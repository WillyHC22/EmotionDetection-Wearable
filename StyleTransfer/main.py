import torch
import torch.optim as optim
from torchvision import models

import numpy as np
from PIL import Image
from tqdm import tqdm
from utils import load_image, get_features, gram_matrix, im_convert
from argparser import get_parser


args = get_parser()

def style_transfer(content_path, style_path, args):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    vgg = models.vgg19(pretrained=True).features
    vgg.to(device)

    for param in vgg.parameters():
        param.requires_grad_(False)

    content = load_image(content_path).to(device)
    style = load_image(style_path, shape=content.shape[-2:]).to(device)

    content_features = get_features(content, vgg)
    style_features = get_features(style, vgg)

    style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

    target = content.clone().requires_grad_(True).to(device)

    style_weights = {'conv1_1': 1.,
                    'conv2_1': 0.75,
                    'conv3_1': 0.2,
                    'conv4_1': 0.2,
                    'conv5_1': 0.2}

    content_weight = args["alpha"] # alpha
    style_weight = args["beta"] # beta

    optimizer = optim.Adam([target], lr=args["learning_rate"]) #Check if this is correct
    steps = args["steps"]  

    for ii in tqdm(range(1, steps+1)):
        
        target_features = get_features(target, vgg)
        
        content_loss = torch.mean((target_features['conv4_2'] - content_features['conv4_2'])**2)

        style_loss = 0

        for layer in style_weights:
            target_feature = target_features[layer]
            target_gram = gram_matrix(target_feature)
            _, d, h, w = target_feature.shape
            style_gram = style_grams[layer]
            layer_style_loss = style_weights[layer] * torch.mean((target_gram - style_gram)**2)
            style_loss += layer_style_loss / (d * h * w)
            
        total_loss = content_weight * content_loss + style_weight * style_loss
        
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        if ii % (steps/10) == 0:
            print('Total loss: ', total_loss.item())

        if ii % args["save_every"] == 0:
            image = im_convert(target)
            im = Image.fromarray((image * 255).astype(np.uint8))
            im.save(f"results/image{ii}.jpg")


if __name__ == '__main__':

    args = get_parser()
    content = args["content"]
    style = args["style"]
    style_transfer(content, style, args)

Implementatio of the style transfer of https://arxiv.org/pdf/1508.06576.pdf using vgg19

Run style transfer on GPU using

CUDA_VISIBLE_DEVICE = x python main.py -c "path_to_content_image" -s "path_to_style_image" -alpha 1 (default) -beta 1e-4 (default)

Play with alpha/beta to generate more or less abstract art according to https://arxiv.org/pdf/1508.06576.pdf


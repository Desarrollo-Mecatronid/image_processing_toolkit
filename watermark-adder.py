import os

def batch_add_watermark(directory, logo):
    print(f'Scanning directory {directory}...')
    print(f'Applying logo {logo} to all images (mock)...')
    return 'Successfully processed 5 images.'

if __name__ == '__main__':
    print(batch_add_watermark('/images/raw/', 'my_brand_logo.png'))
"""
Chapter 04
Python Advanced(4) - 나만의 패키지 만들기 1
Keyword - png(jpg) to gif, pil, image

"""
"""
패키지 작성
정적이미지(png, jpg) > 애니메이션(gif) 이미지 변환 패키지

"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = './project/images/*.png'
path_out = './project/image_out/result.gif'

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹
# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]
# img, *images = [Image.open(f).convert("RGB") for f in sorted(glob.glob(path_in))]

# 리사이즈(필요한 경우)
# img, *images = [Image.open(f).convert("RGB").resize((320,240), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]
# AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'
# PIL.Image.ANTIALIAS는 Pillow 10.0.0 버전부터 제거
# Image.LANCZOS 사용해도 괜찮고 Image.Resampling.LANCZOS로 쓰는 것이 더 최신 코드 스타일이다.
img, *images = [Image.open(f).convert("RGB").resize((320,240), Image.Resampling.LANCZOS) for f in sorted(glob.glob(path_in))]

# 이미지 저장
img.save(
    fp=path_out,
    format='GIF',
    append_images=images,
    save_all=True,
    duration=100,
    loop=0
)
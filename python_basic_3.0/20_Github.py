"""
Chapter 04
Python Advanced(4) - 나만의 패키지 만들기 4 - Github 배포
Keyword - Github package deploy

"""

# py_ad_04_03 : 완성된 패키지 임포트
from py_ad_04_03 import GifConverter as gfc

# 클래스 생성
c = gfc('./project/images/*.png', './project/image_out/result.gif', (320,240))

# 실행
c.convert_gif()

"""
패키지 배포 순서(Github)
1. https://github.com 회원가입
2. git 설치 확인(생략) > .gitignore 파일 고려
3. git add > commit > push
    - git respository : 저장소 생성
    - git init
    - git add
    - git status
    - git commit -m 'message'
    - git remote add origin 'your repository'
    # git remote add origin https://github.com/YYUMMMMMMMM/python_yyummmm.git
    - git push origin master
    
4. PyPI 형태의 패키지 구조를 github repository에 push
5. 설치 확인(pip install git+https://your-repository-url)
# pip install git https://github.com/YYUMMMMMMMM/python_yyummmm.git

"""

"""
프로그래밍은 사람이 사용하는 소프트웨어를 완성하는 것

그래서 어떤 문제를 정하고 이것을 해결하는 과정에서 지식을 습득하는 것의 경력을 쌓는다면

회사에서 요구하는 주니어, 시니어, .. 직급을 가진 디벨로퍼 엔지니어가 된다.

보잘것 없고 하찮은 것도 직접 코딩해보면서 만드는 것을 추천 이러한 과정에서 파생되는 지식의 습득을 무시 못한다.

TDD, 리팩토링, OOP 연습이 중요하다 모든 프로그래밍의 핵심이다!

코드를 작성하는 시간보다 다른 사람의 코드를 읽는 것이 비용이 더 많이 든다.

그렇기에 이해하기 쉽고 각 프로그래밍 언어 특징 원칙에 맞게 가독성이 좋은 코드를 짜는 것이 중요하다.

내 코드를 올려 피드백을 받고, 코드 리뷰를 해줄만한 곳이 깃허브이다.

결국 내가 만든건 다른 사람이 사용한다는 생각을 가지고 코딩을 해야한다.

플랫폼 이해 (AWS, 애거, GCP)

경력자의 경우 트렌디한 기술 발전에 대한 관심을 계속해서 가져야한다.

다양한 오픈소스에서 추가, 변경되는 최신 정보를 유지하려고 노력해야한다.

결정적으로 테스트 디버깅 능력 중요, 레퍼런스 문서를 볼 수 있는 지 중요!

에러 수정 능력은 점진적 코드 리뷰이다 주석과 다이어그램도 중요!

다양한 컨텐츠를 개발하여 반드시 여러 사람과 사이드 프로젝트, 해커톤을 참여하는 것도 중요!

혼자서 하려면 오픈 소스에 참여하는 방법도 있다.

"""
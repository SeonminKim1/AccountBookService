## 🚀 프로젝트 소개
- 주제 : 가게부 서비스
- 기간 : 23.01.04 (화) ~ 23.01.06 (목)   
   

## 🔥 프로젝트 진행

### 📌 1. 요구사항 분석
- 요구사항 세부 분석을 위해 '똑똑가계부', '투데이'의 가계부 어플 레퍼런스 참고
- 전체 서비스를 **회원 서비스 / 가계부 관리 서비스 / 가계부 세부 내역 서비스 / 가계부 카테고리 관리** 4가지로 나누어 요구사항을 작성 
- 정의한 **세부 요구사항은 [Git Issue - 요구사항 분석](https://github.com/SeonminKim1/AccountBookService/issues/1)에 기록**

### 📌 2. DB Table 설계
- DB 설계 내용은 [Git Issue - DB Table 설계](https://github.com/SeonminKim1/AccountBookService/issues/2) 기록
- DB 설계 간 아래 3가지 이슈를 고민하며 설계 (상세 내용은 Github Wiki 에 작성)

  - [DB Table 이름 짓기 : 단수 vs 복수](https://github.com/SeonminKim1/AccountBookService/wiki/DB-Table-%EC%9D%B4%EB%A6%84-%EC%A7%93%EA%B8%B0-:-%EB%8B%A8%EC%88%98-vs-%EB%B3%B5%EC%88%98)
  - [Soft Delete vs Hard Delete](https://github.com/SeonminKim1/AccountBookService/wiki/Soft-Delete-vs--Hard-Delete)
  - [가계부 금액 (AccountBook Price) 필드 값 범위 선정](https://github.com/SeonminKim1/AccountBookService/wiki/%EA%B0%80%EA%B3%84%EB%B6%80-%EA%B8%88%EC%95%A1-(AccountBook-Price)-%ED%95%84%EB%93%9C-%EA%B0%92-%EB%B2%94%EC%9C%84-%EC%84%A0%EC%A0%95)

### 📌 3. 서비스 구현 및 API 설계
- 전체 4가지 서비스 중 **회원 서비스만 API 설계 및 구현** 완료
- [API 설계 링크](https://www.notion.so/API-a4453f4418d1465c8b79570a28e92ee1)
- [x] 회원 서비스 (회원가입 / 로그인, 로그아웃 / JWT Token 인증 관리)
- [ ] 가계부 관리 서비스 (가계부 생성, 조회, 수정, 삭제)
- [ ] 가계부 세부 내역 서비스 
- [ ] 가계부 카테고리 관리 서비스 (카테고리 생성, 조회, 수정, 삭제)


## ✔️ 프로젝트 회고

#### 🛠 프로젝트를 진행하며 가계부 서비스에 대한 방향성에 대한 고민 (vs 은행 어플)
- **은행앱과 가계부 모두 자산관리와 지출/수입 내역, 통계 등을 확인 할 수 있는 공통점**이 존재
- 하지만 가계부는 **특정 이벤트(수신 문자 자동 가계부 등록)나 추가적인 작업이 필요**한 반면, 실시간 조회가 가능한 은행 어플이 좀더 메리트가 있다고 생각
- 가계부의 **장점은 가계부를 직접 기록하면서 지출/수입 등에 되돌아보고 보다 경제적인 생활 습관을 가질 수 있다는 점**
- **is_satisfied 필드**를 가계부 테이블에 두어, **한 번더 고민이 필요한 내역을 모아서 Satisfaction Check 할 수 있는 기능을 기획** 함

#### 🛠 프로젝트를 잘 수행하는 것에 대한 고민
- 처음 3일이란 기한이 주어지고서, 스스로의 **어떤 역량을 프로젝트에 더 잘 드러내야 할 지** 많은 고민을 하였던 것 같습니다. **메인 기능 등을 구현하며, 빠르게 구현 목표를 달성하는 것**과 **완벽한 구현은 아니더라도, 사소한 부분도 계속 고민하며 프로젝트에 임한다는 것** 중 에서 후자의 모습을 조금 더 어필하고 싶었던 것 같습니다. 다만 생각한 목표 구현 범위에 못 미쳤다는 점에서 **기한 내 구현 미션에 밸런스를 유지하지 못한 것은 아닌지, 일정 관리에 있어 예상 못했던 병목 부분(Bug)을 고려하지 못했던 점 등에 대해 회고**하며 앞으로 개선 할 점을 찾는 좋은 계기가 되었던 것 같습니다.


## ⚙️ 프로젝트 셋팅
#### 1. Clone This Repository && environment settings
 ```sh
 $ git clone https://github.com/SeonminKim1/AccountBookService.git
 $ python -m venv accountbook
 $ .\accountbook\Scripts\activate.bat # window
 $ cd AccountBookService
 ```

#### 2. Run Docker Mysql
```sh
$ docker run -p 3306:3306 --name db-mysql2 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=accountbook -v /_docker/db/data:/var/lib/mysql mysql:5.7 --character-set-server=utf8 --collation-server=utf8_unicode_ci
```

#### 3. package install
 ```sh
 $ pip install -r requirements.txt
 ```

4. Make .env.local file
``` ex) .env.local
# Django
SECRET_KEY = <SECRET_KEY>

# DB
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234'
MYSQL_DB_NAME = 'accountbook'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'

#### # TEST USER
ADMIN_USER_NICKNAME = 'SMKIM'
ADMIN_USER_PASSWORD = '1234'
ADMIN_USER_EMAIL = 'yubi5050@naver.com'
```

#### 5. Project migrate & run
 ```sh
 $ python manage.py makemigrations
 $ python manage.py migrate
 $ python _utils/db_base_settings.py # db base setting
 $ python manage.py runserver
 ```

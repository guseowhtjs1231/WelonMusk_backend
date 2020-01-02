import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')


ash_wood_deco = CarInteriors.objects.get(id=1)
dark_wood_deco = CarInteriors.objects.get(id=2)
oak_wood_deco = CarInteriors.objects.get(id=3)
cabon_fiber_deco_1 = CarInteriors.objects.get(id=4)
cabon_fiber_deco_2 = CarInteriors.objects.get(id=5)

model_3_1_all_black = CarInteriors.objects.get(id=6)
model_3_2_black_and_white = CarInteriors.objects.get(id=7)

model_x_1_all_black = CarInteriors.objects.get(id=8)
model_x_2_black_and_white = CarInteriors.objects.get(id=9)
model_x_3_cream = CarInteriors.objects.get(id=10)

model_s_ash_wood_desc = "<div><ul><li>Tesla의 조용한 실내에 맞춰 특별히 튜닝된 프리미엄 오디오 시스템</li><li>전좌석 열선 시트, 열선 스티어링 휠, 와이퍼 블레이드 서리 제거 장치 및 워셔 노즐 히터를 포함한 동절기 기능</li><li>HEPA 필터 시스템을 이용한 바이러스, 박테리아 및 악취의 실내 침투 방지</li><li>프리미엄 커넥티비티 (1년 제공)<ul><li>실시간 교통 상황을 나타내는 위성 지도</li><li>차량 내 인터넷 스트리밍 음악 및 미디어</li><li>셀룰러를 이용한 주기적인 OTA(Over-the-air) 업데이트</li><li>인터넷 브라우저</li></ul></li><li>Bluetooth®를 통한 음악 및 미디어 재생</li><li>LED 안개등</li><li>자외선 및 적외선 보호장치가 장착된 틴티드 글래스 루프</li><li>자동 조도 조절, 전동식 폴딩이 가능한 열선 사이드 미러</li><li>사용자 지정 운전자 프로필</li></ul></div>"


model_3_for_1_all_black_desc = "<div><ul><li>12방향 전동 조절식 앞좌석 열선 시트</li><li>프리미엄 시트 소재 및 트림</li><li>오디오 업그레이드 – 높은 몰입도의 사운드</li><li>Bluetooth®를 통한 음악 및 미디어 재생</li><li>자외선 및 적외선 보호장치가 장착된 틴티드 글래스 루프</li><li>자동 조도 조절, 전동식 폴딩이 가능한 열선 사이드 미러</li><li>사용자 지정 운전자 프로필</li><li>수납 공간, 4개의 USB 포트 및 2개의 스마트폰 도킹을 포함한 센터 콘솔</li></ul></div>"
model_3_for_2_black_and_white_desc = "<div><ul><li>12방향 전동 조절식 앞좌석 열선 시트</li><li>프리미엄 시트 소재 및 트림</li><li>오디오 업그레이드 – 높은 몰입도의 사운드</li><li>자외선 및 적외선 보호장치가 장착된 틴티드 글래스 루프</li><li>자동 조도 조절, 전동식 폴딩이 가능한 열선 사이드 미러</li><li>Bluetooth®를 통한 음악 및 미디어 재생</li><li>사용자 지정 운전자 프로필</li><li>수납 공간, 4개의 USB 포트 및 2개의 스마트폰 도킹을 포함한 센터 콘솔</li></ul></div>"


model_x_common_desc = "<div><ul><li>자동 프리젠팅 및 클로징 전면 도어</li><li>Tesla의 조용한 실내에 맞춰 특별히 튜닝된 프리미엄 오디오 시스템</li><li>전좌석 열선 시트, 열선 스티어링 휠, 와이퍼 블레이드 서리 제거 장치 및 워셔 노즐 히터를 포함한 동절기 기능</li><li>HEPA 필터 시스템을 이용한 바이러스, 박테리아 및 악취의 실내 침투 방지</li><li>프리미엄 커넥티비티 (1년 제공)<ul><li>실시간 교통 상황을 나타내는 위성 지도</li><li>차량 내 인터넷 스트리밍 음악 및 미디어</li><li>셀룰러를 이용한 주기적인 OTA(Over-the-air) 업데이트</li><li>인터넷 브라우저</li></ul></li><li>Bluetooth®를 통한 음악 및 미디어 재생</li><li>LED 안개등</li><li>자외선 및 적외선 보호 기능을 갖춘 파노라마 윈드실드</li><li>자동 조도 조절, 전동식 폴딩이 가능한 열선 사이드 미러</li><li>사용자 지정 운전자 프로필</li></ul></div>"


CarInteriorPrices.objects.create(model = model_s, interior = ash_wood_deco, interior_price= 0, descriptions=model_s_ash_wood_desc)
CarInteriorPrices.objects.create(model = model_s, interior = dark_wood_deco, interior_price= 1968000, descriptions=model_s_ash_wood_desc)
CarInteriorPrices.objects.create(model = model_s, interior = oak_wood_deco, interior_price= 1968000, descriptions=model_s_ash_wood_desc)
CarInteriorPrices.objects.create(model = model_s, interior = cabon_fiber_deco_1, interior_price= 656000, descriptions=model_s_ash_wood_desc)
CarInteriorPrices.objects.create(model = model_s, interior = cabon_fiber_deco_2, interior_price= 2624000, descriptions=model_s_ash_wood_desc)


CarInteriorPrices.objects.create(model = model_3, interior = model_3_1_all_black, interior_price= 0, descriptions=model_3_for_1_all_black_desc)
CarInteriorPrices.objects.create(model = model_3, interior = model_3_2_black_and_white, interior_price= 1286000, descriptions=model_3_for_2_black_and_white_desc)


CarInteriorPrices.objects.create(model = model_x, interior = model_x_1_all_black, interior_price= 0, descriptions=model_x_common_desc)
CarInteriorPrices.objects.create(model = model_x, interior = model_x_2_black_and_white, interior_price= 1968000, descriptions=model_x_common_desc)
CarInteriorPrices.objects.create(model = model_x, interior = model_x_3_cream, interior_price= 1968000, descriptions=model_x_common_desc)
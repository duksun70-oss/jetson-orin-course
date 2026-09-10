# Week 13 Lab — 객체 반응형 AMR

## 시나리오 예
사람 또는 지정 객체가 일정 조건으로 검출되면 감속/정지한다.

## 절차
1. Detector output을 ROS 2 message로 전달.
2. Decision node에 상태 정의: NORMAL/SLOW/STOP/FAULT.
3. confidence 및 timeout 조건 설정.
4. 시뮬레이터 또는 저속 실기에서 검증.
5. 오검출/미검출 시 안전 동작 확인.

## 제출
상태도, Topic 구조, 시험결과.
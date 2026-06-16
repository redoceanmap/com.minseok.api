# CLAUDE.md — Titanic 앱

백엔드 규칙 → [[vault/minseok/CLAUDE|minseok CLAUDE]]

---

## 도메인 용어 (등장인물 → 역할 매핑)

| 등장인물 | 역할 |
|----------|------|
| Smith (선장) | 전체 오케스트레이션 · 채팅 진입점 |
| Jack | ML 모델 훈련 (Trainer) |
| Rose | ML 모델 추론 (Model) |
| Andrews | 아키텍처 설계 / 파이프라인 구성 (Architect) |
| Molly | 피처 스케일링 (Scaler) |
| Cal | 모델 테스트 / 평가 (Tester) |
| Ruth | 데이터 검증 (Validation) |
| Isidor | 커플(앙상블) 모델 (Couple) |
| James | 전체 디렉터 / 실험 관리 (Director) |
| Lowe | 구명보트 / 체크포인트 저장 (Boat) |
| Hartley | 바이올린 / 로그 · 모니터링 (Violin) |
| Walter | 로스터 / 배치 스케줄러 (Roaster) |

새 역할 추가 시 이 테이블을 먼저 업데이트한다.

---

## 레이어별 파일 네이밍

```
<등장인물_역할>.py  예) crew_smith_captain_router.py
                       passenger_jack_trainer_interactor.py
```

- `crew_` 접두사: 선원 (핵심 시스템 역할)
- `passenger_` 접두사: 승객 (ML 파이프라인 역할)

---

## 앱 내부 임포트 예시

```python
# 같은 앱 내부 — 반드시 titanic. 으로 시작
from titanic.app.ports.input.passenger_jack_trainer_use_case import JackTrainerUseCase
from titanic.domain.value_objects.crew_smith_captain_vo import SmithCaptainVO
```

`minseok.apps.titanic.` 형태는 사용하지 않는다 (컨테이너 경로 불일치).


##타이타닉 도메인 문서 연결

- 타이타닉 도메인 문서 연결
- 타이타닉 피처 정리 : [[titanic-features]]
- 타이타닉 머신러닝 : [[titanic-machine-learning]]
- 타이타닉 ERD : [[titanic-erd]]
- 타이타닉 NF : [[titanic-nf]]
- 타이타닉 알고리즘 : [[titanic-algorithm]]
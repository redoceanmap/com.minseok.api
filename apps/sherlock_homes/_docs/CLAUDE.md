# CLAUDE.md — Sherlock Homes 앱

---

## 도메인 용어 (등장인물 → 역할 매핑)

새 역할 추가 시 이 테이블을 먼저 업데이트한다.

---

## 레이어별 파일 네이밍

```
<등장인물_역할>.py
```

---

## 앱 내부 임포트 예시

```python
from sherlock_homes.app.ports.input.xxx_use_case import XxxUseCase
```

`minseok.apps.sherlock_homes.` 형태는 사용하지 않는다 (컨테이너 경로 불일치).


# Feature selection

Feature selection은 머신러닝 및 데이터 분석에서 중요한 단계 중 하나로, 모델에 가장 유의미한 특징(또는 변수)들을 선택하는 과정입니다. 이러한 선택은 모델의 성능을 향상시키고, 계산 비용을 줄여줄 수 있습니다.

보통 RandomForest Classifier의 feature importance_를 사용하는 경우가 많은데 information value랑 woe에 대해서 알아보자.

두 지표는 feature selection과 관련하여 변수의 중요도를 측정하는 지표입니다. 둘은 비슷하면서 다른 점이 존재함으로 차이를 명확하게 하고 가는 것이 좋을 것 입니다.

## Weight of Evidence(WOE) 근거의 무게

종속 변수(target col)와 관련하여 영향력 있는 독립 변수의 예측력을 나타내는 지표입니다.

여기서 이벤트(event)라는 개념이 존재하는데 로지스틱 회귀(이항 분류)에서 사용되던 것으로 두 개중의 하나의 class 혹은 label로 생각할 수 있다. 신용평가 자료에서의 경우람녀 고객이 신용채무능력이 있는 경우를 non-event, 없는 경우를 event라고 표현할 수 있을 것이다.

값이 양수이면 좋은 고객(non-event)의 비율이 나쁜 고객(event)의 비율보다 큰 것이다.

$$
WOE = ln \genfrac [] {1pt}{1}{\text{Distribution of goods}}{\text{Distribution of bads}} = ln \genfrac [] {1pt}{1}{\text{\% of non-events}}{\text{\% of events}}
$$

1. 연속형 변수인 경우, 데이터를 10개의 구간으로 binning. qcut
2. 각 그룹의 이벤트, 비이벤트의 수를 계산
3. 그들의 비율 계산
4. 자연 로그(ln) -> 구간별 woe를 계산

종속변수의 분포 유사성(event, non-evnet count)에 기초하여 연속적인 독립변수를 하나의 범주로 변환하는데 사용한다. 뭔소린지 모르겠다.

## Information value 정보가치

위에서 사용한 WOE의 events, non-event의 분포를 사용하여 구하게 된다.

1. 변수의 값들을 일정한 구간(bin)으로 나눕니다.
2. 각 구간에 속한 관측치의 수와 목표 변수의 이벤트(예: 양성 클래스)가 발생한 횟수를 계산합니다.
3. 각 구간의 비율과 비율의 로그값을 계산합니다.
4. 각 구간의 정보 가치를 계산하기 위해 구간 비율과 로그값을 곱한 후, 모든 구간의 정보 가치를 합산합니다.

$$
IV = \sum(\text{\% of non-events} - \text{\% of events}) * WOE
$$

정보 가치는 변수와 목표 변수 간의 상관 관계를 나타내는 수치로 사용됩니다. 정보 가치가 높은 변수는 feature selection에서 우선적으로 선택되는 경향이 있습니다.
Information value는 변수의 중요도를 측정하는 하나의 방법이지만, 다른 특징 선택 기법과 함께 사용될 수도 있습니다. 변수 간의 다중공선성을 고려하여 상호 관련된 변수 중 하나만 선택하는 등의 추가적인 고려 사항이 필요할 수 있습니다.
하나만 선택하는 등의 추가적인 고려 사항이 필요할 수 있다.

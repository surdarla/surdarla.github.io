- 멘토링 신청 DAM-MN-030402
  - cnst/mntrgReqstList.html
    - 입장 : 개인(아이디)가 신청한 멘토링이 전부 나와야 한다.
    - 제목 클릭 : 개인이 신청한 멘토링을 수정할 수 있는 화면(cnst/mntrgReqst)으로 간다.
    - 등록 클릭 : 개인이 새로운 멘토링을 신청할 수 있는 화면(cnst/mntrgReqst)으로 간다.
  - cnst/mntrgReqst.do
    - 수정 클릭 : 제목 클릭한 화면에서 데이터를 수정하고 누르면 updated된다.
    - 등록 클릭 : 콘테스트 분야를 선택하고 새로운 멘토링 신청을 insert한다.

- 멘토링 배분/답변/게시 처리 DAM-MN-030801
    - cnst/mntrgList.html
      - 메뉴에서 `멘토링` -> `온라인 멘토링`을 눌러서 들어간다.
      - 기본적으로는 개인의 온라인 멘토링들이 나열된다.
      - 콤보박스에서 콘테스트, 분야, 상태를 선택하여 검색을 한다.
      - 제목을 누르면 해당 멘토링 배분/답변/게시 처리로(cnst/mntrgAns)으로 이동
    - cnst/mntrgAns.html
      - 해당 멘토링 신청

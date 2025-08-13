```mermaid
flowchart LR
  %% --- Lanes ---
  subgraph L[Local]
    direction TB
    L1["html\nFlask"] --> L2[OPEN]
    %% 입출력
    L3["채팅 text\n요청"] -->|json 요청| W1
    W2 -->|json 응답| L4["채팅 text"]
    L5[Input] --> L6[model] --> L7[output] --> L8["대답 text"]
    L8 -->|json| W3
    %% 부정 단어 감지 후 카카오
    D1{"부정적 단어\n7회 이상?"}
    L8 --> D1
  end

  subgraph W[Web Server]
    direction TB
    W0[OPEN]
    W4["채팅 text\njson 저장"]
    W1["채팅 text\n요청받음"]
    W2["채팅 text"]  %% 응답용
    W3["대답 text"] --> P1
  end

  subgraph P[Web Page]
    direction TB
    P0[OPEN]
    P2[채팅입력] --> P3[채팅창 출력] --> W4
    P1 --> C{"응답 수신?"}
    C -->|True| P4["대답 text"]
    C -->|False| P5["죄송합니다.\n서버연결에 실패했습니다."]
  end

  subgraph K[카카오]
    direction TB
    K1["카카오\n메시지 전송"]
  end

  %% --- Cross-lane links ---
  L2 --> W0 --> P0
  D1 -->|Yes| K1
  D1 -->|No| P1
```

# Campaign Strategy Route

Research-tool launch campaign demo

```mermaid
flowchart LR
  title["Campaign Strategy Route"]
  subgraph audience["Audience"]
    audience_segments["Map user segments"]
  end
  subgraph insight["Insight"]
    insight_editable["Lead with editability"]
  end
  subgraph message["Message"]
    message_positioning["Position workflow value"]
    message_proof["Show before and after"]
  end
  subgraph channels["Channels"]
    channels_github["Use GitHub as hub"]
    channels_content["Publish demo content"]
  end
  subgraph measurement["Measurement"]
    measurement_metrics["Track adoption signals"]
    measurement_optimize["Optimize message route"]
  end
  audience_segments -->|reveals| insight_editable
  insight_editable -->|shapes| message_positioning
  message_positioning -->|proves| message_proof
  message_proof -->|anchors| channels_github
  channels_github -->|extends| channels_content
  channels_content -->|drives| measurement_metrics
  measurement_metrics -->|feeds back| measurement_optimize
  measurement_optimize -->|iterates| message_positioning
```

## Route Evidence

| Stage | Node | Evidence |
|---|---|---|
| Audience | Map user segments | document - examples/campaign-route-demo/source/campaign-brief.md - Audience |
| Insight | Lead with editability | document - examples/campaign-route-demo/source/campaign-brief.md - Insight |
| Message | Position workflow value | document - examples/campaign-route-demo/source/campaign-brief.md - Strategy |
| Message | Show before and after | document - examples/campaign-route-demo/source/campaign-brief.md - Creative route |
| Channels | Use GitHub as hub | document - examples/campaign-route-demo/source/campaign-brief.md - GitHub README and templates |
| Channels | Publish demo content | document - examples/campaign-route-demo/source/campaign-brief.md - Channel route |
| Measurement | Track adoption signals | document - examples/campaign-route-demo/source/campaign-brief.md - Measurement |
| Measurement | Optimize message route | document - examples/campaign-route-demo/source/campaign-brief.md - Optimization |

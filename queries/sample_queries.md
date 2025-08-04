#  Sample CloudWatch Logs Insights Queries & Prompts

This file provides practical examples of CloudWatch Logs Insights queries alongside the natural language prompts used in the Query Assistant. These examples are based on logs generated from a sample AWS Lambda function. All queries are Free Tier–friendly if used with narrow time windows (e.g., last 5–15 minutes).

---

## 1. Basic Log Exploration

### Prompt:
> Show me all logs from the last 15 minutes

```sql
fields @timestamp, @message
| sort @timestamp desc
| limit 20

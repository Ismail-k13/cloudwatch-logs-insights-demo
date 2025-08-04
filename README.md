## Full Walkthrough: From Setup to Querying Logs with AWS CloudWatch Logs Insights Query Assistant

This section documents the complete process of setting up a logging Lambda function, generating logs, and using AWS CloudWatch Logs Insights Query Assistant to analyze the logs using natural language queries — all within the AWS Free Tier.

---

### 1. **Project Objective**

The goal is to demonstrate how to:

* Create a Lambda function that emits logs at different severity levels
* View those logs in CloudWatch
* Use the Query Assistant to explore log data with natural language
* Translate prompts into structured queries for filtering, parsing, and aggregation

---

### 2. **Environment Setup**

####  AWS Requirements

* AWS Free Tier account
* IAM permissions to create Lambda functions, CloudWatch Logs access

---

### 3. **Create the Lambda Function**

#### a. Go to AWS Lambda Console

* Select **Create function**
* Choose **Author from scratch**
* Fill in:

  * Function name: `LogGeneratorLambda`
  * Runtime: `Python 3.12` (or latest available)
  * Permissions: Create a new role with basic Lambda permissions

#### b. Replace the Lambda Code

Paste the following code in the inline editor:

```python
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("INFO level: Lambda executed successfully.")
    logger.warning("WARNING level: This is a sample warning.")
    logger.error("ERROR level: This is a sample error.")
    return {
        'statusCode': 200,
        'body': 'Log event generated.'
    }
```

#### c. Deploy and Test

* Click **Deploy**
* Click **Test**, configure a test event (can be blank JSON)
* Run the test 3–5 times to generate enough log data

---

### 4. **View Logs in CloudWatch**

1. Go to **CloudWatch Console**
2. Navigate to **Log groups**
3. Locate the log group (e.g., `/aws/lambda/LogGeneratorLambda`)
4. Click into the stream to verify the logs were created:

   * INFO
   * WARNING
   * ERROR

---

### 5. **Use CloudWatch Logs Insights**

1. Open **CloudWatch Logs Insights** from the CloudWatch sidebar
2. Select the log group (`/aws/lambda/LogGeneratorLambda`)
3. Choose a time range (e.g., last 30 minutes)
4. Confirm that logs exist

---

### 6. **Use the Query Assistant**

1. Click the **Ask a question** tab in the Logs Insights Console
2. Enter natural language prompts like:

   * “Show ERROR logs only”
   * “Count logs by severity”
   * “Display logs sorted by timestamp”
3. Review the generated query
4. Click **Run query** to see results

If you see errors like:

```
Query's end date and time is either before the log group's creation time or exceeds the log group's log retention settings
```

→ Make sure your selected time range includes when the function was executed and that logs are available.

---

### 7. **Write and Save Reusable Queries**

You can create a file like `queries/sample-queries.md` to keep reusable prompts and their generated queries. Example:

```sql
-- Count logs by level
fields @message
| parse @message "* level: *" as level
| stats count() by level
```

---

### 8. **Organize Your Project**

Folder layout:

```
cloudwatch-logs-insights-demo/
├── lambda/
│   └── sample_logger.py
├── queries/
│   └── sample-queries.md
├── screenshots/            # Optional
├── README.md
└── .gitignore
```

You can also include screenshots for visual steps.

---

### 9. **Cleanup**

To avoid unnecessary AWS charges:

* Delete the Lambda function from the Lambda console
* Delete the log group from CloudWatch
* Delete the IAM role created for the Lambda (optional if unused elsewhere)

---

### 10. **Summary**

This walkthrough covers the full lifecycle:

* Creating and running a logging Lambda
* Viewing logs in CloudWatch
* Using the Logs Insights Query Assistant
* Writing and managing queries

This process enables DevOps, Cloud, and Developer teams to easily explore logs, perform root cause analysis, and integrate structured logging into serverless applications — without needing prior knowledge of the query language.

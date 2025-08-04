The `cleanup.md` file provide **step-by-step instructions to clean up all AWS resources** created during the demo, so that users **avoid unnecessary charges** and keep their AWS account tidy.

Here’s a complete `cleanup.md` you can use:

---

## 🧹 Cleanup Guide

To avoid ongoing AWS charges and ensure your environment remains clean after using this project, follow the steps below to remove all associated resources.

---

###  Resources to Delete

| Resource Type       | Name / Identifier                   | Delete From        |
| ------------------- | ----------------------------------- | ------------------ |
| Lambda Function     | `LogGeneratorLambda`                | AWS Lambda Console |
| Log Group           | `/aws/lambda/LogGeneratorLambda`    | CloudWatch Logs    |
| IAM Role (Optional) | `LogGeneratorLambda-execution-role` | IAM Console        |

---

### 🧾 Step-by-Step Cleanup Instructions

---

### 1. **Delete the Lambda Function**

* Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/)
* Locate the function named `LogGeneratorLambda`
* Select it, click **Actions > Delete**
* Confirm deletion

---

### 2. **Delete the CloudWatch Log Group**

* Go to the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/)
* In the left sidebar, click **Logs > Log groups**
* Search for `/aws/lambda/LogGeneratorLambda`
* Select it and click **Actions > Delete log group**
* Confirm deletion

---

### 3. **Delete the IAM Role (Optional)**

> Do this **only if you’re sure** the IAM role is not reused elsewhere.

* Go to the [IAM Console](https://console.aws.amazon.com/iam/)
* In the left sidebar, click **Roles**
* Search for a role named something like `LogGeneratorLambda-role-xxxx`
* Click on the role and verify it’s only used by this Lambda
* Click **Delete**

---

###  Best Practices After Cleanup

* Double-check your **CloudWatch metrics and billing** dashboard for any leftover activity.
* If you're exploring AWS often, consider setting up [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets) to monitor Free Tier usage and get alerts.

---

###  Questions or Issues?

If you're unsure whether a resource is safe to delete, check the [AWS Resource Explorer](https://console.aws.amazon.com/resource-explorer/) or ask in the [AWS Developer Forums](https://forums.aws.amazon.com/).



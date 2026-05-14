# Vision and Plan: Exploring Python for Infrastructure Automators

## 1. The Core Vision
**Exploring Python** will pivot from a generic "Intro to Computer Science" resource to a specialized **"Script to System"** guide. It targets IT professionals, Sysadmins, and Platform Engineers who are already technical but need to build backend components, automation tools, and "glue code" for the systems they manage.

**The Goal:** Transform Python from "just another language" into the essential connective tissue between **Exploring Enterprise Linux** (System Administration) and **Exploring Kubernetes** (Platform Engineering).

## 2. The Persona: "The Infra Automator"
*   **Background:** Sysadmin, Network Engineer, Platform Engineer, or DevOps.
*   **Context:** Already comfortable in a terminal; likely knows Bash.
*   **Mental Model:** Sees Python as "High-Performance Bash" or "Structured Automation."
*   **Pain Points:** 
    *   "It worked on my machine but failed in CI."
    *   "I have a 500-line shell script that is impossible to maintain."
    *   "I need to parse complex JSON/YAML from an API and Bash is too hard."
    *   "I don't need to know Bubble Sort; I need to know how to restart a service if it hangs."

## 3. The "Script to System" Progression
The site will be restructured from `Basics/Intermediate/Advanced` to a progressive **Day One → Level 6** journey.

### **Day One: The Clean Setup (Environment)**
*   **Goal:** Stop "Python Hell" before it starts.
*   **Key Topics:**
    *   Installing Python correctly (not using the system Python).
    *   **Virtual Environments (`venv`)**: The non-negotiable standard.
    *   **Dependency Management (`pip`)**: `requirements.txt` vs. reality.
    *   **The REPL**: Your scratchpad for testing ideas.

### **Level 1: Parsing the Noise (Data as Inventory)**
*   **Goal:** Treating text, logs, and config data as manageable objects.
*   **Reframed Topics:**
    *   **Strings**: Parsing log lines, f-strings for clean CLI output (vs. `echo`).
    *   **Lists**: Managing server inventories, pod lists, file paths.
    *   **Dictionaries**: Handling JSON configs, key-value lookups (IP addresses, tags).
    *   *Approach: No abstract math examples. Use IP addresses, hostnames, and status codes.*

### **Level 2: Automating Decisions (Logic)**
*   **Goal:** Replacing manual checklists with code logic.
*   **Reframed Topics:**
    *   **If/Else**: Deployment gates (e.g., "If disk > 90%, do X").
    *   **Loops**: Batch processing (e.g., "For each server in inventory...").
    *   **Comprehensions**: Filtering resources (e.g., "Get all pods where status != Running").

### **Level 3: From Script to Tool (Structure)**
*   **Goal:** Moving from fragile "scripts" to maintainable "tools."
*   **Reframed Topics:**
    *   **Functions**: Don't repeat yourself; isolate logic.
    *   **Modules & Imports**: Breaking that 500-line file into logical chunks.
    *   **Argument Parsing (Basic)**: Moving away from hardcoded variables.

### **Level 4: Touching the System (The "Ops" Level)**
*   **Goal:** Interacting with the OS (Replacing complex Bash).
*   **Reframed Topics:**
    *   **`pathlib`**: Modern file system handling (vs. `rm -rf`).
    *   **`os` / `shutil`**: Environment variables, file operations.
    *   **`subprocess`**: Running shell commands safely from Python.
    *   **`json` & `yaml`**: Reading/Writing the languages of Infrastructure.
    *   *Linkage:* Deep references to `exploring_linux` concepts (permissions, paths).

### **Level 5: Talking to the World (Integration)**
*   **Goal:** Robust interaction with external systems.
*   **Reframed Topics:**
    *   **`requests`**: Talking to APIs (Cloud, K8s, GitHub).
    *   **Error Handling (`try/except`)**: failing gracefully, not crashing.
    *   **Logging**: Structured logging vs. `print()` debugging.

### **Level 6: Production Grade (Shipping)**
*   **Goal:** delivering professional-grade tooling.
*   **Reframed Topics:**
    *   **CLIs**: Building proper command-line tools (`click` or `argparse`).
    *   **Testing**: Basic Unit Tests (`pytest`) to ensure the script works.
    *   **Packaging**: Dockerizing Python scripts for K8s jobs.
    *   *Linkage:* Preparing tools to be deployed in `exploring_kubernetes`.

## 4. Strategic Alignment
*   **Visual Language:** Adoption of **Mermaid Diagrams** for workflows and **Card Grids** for context (Why > How).
*   **Editorial Tone:** "Mentorship" tone. Acknowledgement of the "IT Trenches."
*   **Cross-Referencing:** 
    *   Level 4 explicitly relies on **Linux** knowledge.
    *   Level 6 explicitly prepares tools for **Kubernetes** deployment.

---

## 5. Task-First Content Plan

The old Level 1-6 concept-first structure is superseded. Every article title is a task or scenario, not a topic. The Python concepts appear in service of the task.

### 📦 Essentials — planned articles

| Title | File | Core concept taught |
|-------|------|-------------------|
| Which Pods Aren't Running? | `essentials/pods_not_running.md` | Dict filtering from kubectl JSON |
| Find the One Field You Need | `essentials/api_response_filtering.md` | Nested dict navigation from API responses |
| Which EC2 Instances Have No Name Tag? | `essentials/aws_tag_audit.md` | AWS CLI JSON filtering, same pattern as above |
| Is My Cert Going to Expire? | `essentials/cert_expiry.md` | SSL expiry check across a list of domains |
| Summarize the Admission Controllers | `essentials/admission_controllers.md` | Two k8s resource types, structured output |

### ⚡ Efficiency — planned articles

| Title | File | Core concept taught |
|-------|------|-------------------|
| Is This Whole Stack Healthy? | `efficiency/stack_health.md` | Multi-endpoint checks, `click` CLI, table output |
| What Changed Between Deploys? | `efficiency/diff_deploys.md` | Comparing two manifests or Helm values files |
| Which Repos Are Missing CODEOWNERS? | `efficiency/repo_audit.md` | GitHub API, pagination |
| Is There an Active Incident? | `efficiency/incident_check.md` | PagerDuty/OpsGenie API, deployment gating |
| Send a Slack Message When the Deploy Finishes | `efficiency/slack_notify.md` | Webhooks, simple integrations |
| Which Namespaces Have No Resource Limits? | `efficiency/namespace_audit.md` | K8s audit, ResourceQuota/LimitRange |
| Parse Logs With Regular Expressions | `efficiency/regex_logs.md` | `re` module for non-standard log formats |

### 🎯 Mastery — planned articles

| Title | File | Core concept taught |
|-------|------|-------------------|
| Reconcile Git vs Deployed | `mastery/git_vs_deployed.md` | GitOps drift detection |
| Daily Cost Report by Team Tag | `mastery/cost_report.md` | AWS Cost Explorer API, Slack output |
| Is This Namespace Production-Ready? | `mastery/namespace_readiness.md` | Multi-resource audit, checklist output |
| Rotate a Service Account Token | `mastery/rotate_tokens.md` | Multi-cluster ops, Vault integration |
| Parse Terraform State | `mastery/terraform_state.md` | `terraform show -json`, resource inventory |

---

## 6. Cross-Link Opportunities

Published pages on sister sites as of May 2026. Link to these from Python articles where relevant.

### → k8s.bradpenney.io

| Python article | Links to |
|----------------|----------|
| `health_check.md`, `run_everywhere.md`, `wrapping_bash.md` | [kubectl commands](https://k8s.bradpenney.io/day_one/kubectl/commands/), [understanding kubectl](https://k8s.bradpenney.io/day_one/kubectl/understanding/) |
| `essentials/yaml.md` | [kubectl first deploy](https://k8s.bradpenney.io/day_one/kubectl/first_deploy/) — applying manifests |
| Future: pods_not_running, admission_controllers | [what is kubernetes](https://k8s.bradpenney.io/day_one/what_is_kubernetes/) |

### → linux.bradpenney.io

| Python article | Links to |
|----------------|----------|
| `parsing_logs.md` | [reading logs](https://linux.bradpenney.io/day_one/reading_logs/), [grep](https://linux.bradpenney.io/essentials/grep/) |
| `run_everywhere.md` | [processes](https://linux.bradpenney.io/essentials/processes/), [users and groups](https://linux.bradpenney.io/essentials/users_and_groups/) |
| `wrapping_bash.md` | [pipes and redirection](https://linux.bradpenney.io/essentials/pipes_and_redirection/), [command line fundamentals](https://linux.bradpenney.io/essentials/command_line_fundamentals/) |
| `safety_guide.md` | [linux safety guide](https://linux.bradpenney.io/day_one/safety_guide/) |
| Future: cert_expiry | [file permissions](https://linux.bradpenney.io/essentials/file_permissions/) |

### → cs.bradpenney.io

| Python article | Links to |
|----------------|----------|
| Future: regex_logs | [regular expressions (essentials)](https://cs.bradpenney.io/essentials/regular_expressions/), [regular expressions (efficiency)](https://cs.bradpenney.io/efficiency/regular_expressions/) |
| `essentials/yaml.md` | [how parsers work](https://cs.bradpenney.io/efficiency/how_parsers_work/) |
| Future: api_response_filtering | [lists recursive structure](https://cs.bradpenney.io/efficiency/lists_recursive_structure/) |

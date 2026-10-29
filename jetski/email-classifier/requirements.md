# Requirements: email-classifier skill

## 1. Scope

The Jetski skill `email-classifier` classifies unread messages in the Gmail inbox according to a database of generic topic classes, computes their importance, and performs the actions assigned to the classes.

Module abbreviation: `EMC`.

Parent requirements: the user's global rules (rule `user_global`) and the skill authoring rules of the Jetski `skill-creator` skill (`~/.gemini/config/skills/skill-creator/SKILL.md`).

Definitions:

- **User** — owner of the Gmail mailbox and sole decision authority.
- **Main thread** — the agent instance that started the skill and coordinates the work.
- **Subagent** — an agent started by the main thread to evaluate a group of messages.
- **Topic Database** — the JSON file holding the Topic Class Collection.
- **Database Template** — the JSON file shipped with the skill from which a missing Topic Database is created.
- **Topic Class Collection** — the list of all topic classes in the Topic Database.
- **Topic Class** — one entry of the Topic Class Collection.
- **Topic Class Identifier** — the unique identifier of a Topic Class.
- **Topic Class Name** — the short name of a Topic Class.
- **Topic Class Description** — the scope description of a Topic Class.
- **Topic Class Weight** — the weight of a Topic Class used in the Message Importance Score.
- **Class-Specific Content Scoring Instructions** — the instructions of a Topic Class for determining the Content Importance Score.
- **Autonomous Action Threshold** — the Message Importance Score limit of a Topic Class that separates the Below-Threshold Action List from the Above-Threshold Action List.
- **Below-Threshold Action List** — the action of a Topic Class for a Message Importance Score less than or equal to the Autonomous Action Threshold.
- **Above-Threshold Action List** — the action of a Topic Class for a Message Importance Score greater than the Autonomous Action Threshold.
- **Message Urgency Score** — the urgency score of a message.
- **Content Importance Score** — the content importance score of a message.
- **Message Importance Score** — the result of Message Urgency Score + (Topic Class Weight × Content Importance Score).
- **Importance Calculation** — the textual record of the Message Importance Score computation showing its operands and result.
- **Mail Tool Command Entry** — an action entry starting with `gmail `.
- **Semantic Instruction Entry** — an action entry starting with `prompt: `.
- **Message Identifier Placeholder** — the marker `{ID}` in a Mail Tool Command Entry.
- **Unknown Topic Class Marker** — the value that marks a message matching no Topic Class.
- **Class Proposal** — a proposed Topic Class for a message marked with the Unknown Topic Class Marker.
- **Message Evaluation Record** — the per-message data a subagent passes to the scoring script.
- **Message Outcome Record** — the per-message result a subagent returns to the main thread.
- **Deferred Semantic Action List** — the list of Semantic Instruction Entries returned by the scoring script for execution by a subagent.
- **Range Error List** — the list of messages whose Message Evaluation Record contains out-of-range data, with the problems found.
- **Processing Mode** — one of: Autonomous Mode (Below-Threshold Action List selected), Escalated Mode (Above-Threshold Action List selected), Unknown Topic Mode (message marked with the Unknown Topic Class Marker).
- **Scoring script** — the Python script that computes the Message Importance Score and executes Mail Tool Command Entries.
- **Validation script** — the Python script that checks the Topic Database.
- **gmail CLI** — the program `/google/bin/releases/gemini-agents-gmail/gmail`.
- **MESSAGE_ID** — a message identifier returned by the gmail CLI.
- **Default Content Scoring Scale** — the content scoring scale stored in the skill: 0.0 — outdated message or duplicate superseded by a newer message; 0.1–0.2 — automated digest, rotation summary, mass newsletter, bot notification requiring no action; 0.3–0.5 — FYI on a broad alias, meeting notes, routine status; 0.6–0.8 — significant project discussion, direct code review, technical question to the team; 0.9–1.0 — critical change, blocker, escalation, task addressed to the user by name.

## 2. Functional requirements

### 2.1 Topic database

- REQ-EMC-1.1: The Topic Database shall be a JSON file at the path `~/.gemini/email_topics.json`.
- REQ-EMC-1.2: The Topic Database shall store the Topic Class Collection in its top-level object.
- REQ-EMC-1.3: Each Topic Class shall contain a Topic Class Identifier, Topic Class Name, Topic Class Description, Topic Class Weight, Class-Specific Content Scoring Instructions, Autonomous Action Threshold, Below-Threshold Action List, and Above-Threshold Action List.
- REQ-EMC-1.5: The Topic Class Weight shall be a number in the range 0.0–1.0.
- REQ-EMC-1.7: The Class-Specific Content Scoring Instructions shall be a text; an empty text is permitted.
- REQ-EMC-1.8: A Topic Class shall describe a generic category of conversations or an entire project, not a single thread.
- REQ-EMC-1.11: The Autonomous Action Threshold shall be a number in the range 0.00–2.00.
- REQ-EMC-1.12: When the Topic Database does not exist, the main thread shall create it with an empty Topic Class Collection.
- REQ-EMC-1.13: The Database Template shall contain an empty Topic Class Collection and no example Topic Classes.
- REQ-EMC-1.14: The skill shall provide example Topic Classes in a file separate from the Database Template that the skill instructions do not reference.
- REQ-EMC-1.15: The Topic Class Identifier shall consist of one or more characters, each being an uppercase letter A–Z, a digit, an underscore, or a hyphen, without spaces, and shall be unique within the Topic Database.
- REQ-EMC-1.16: The Topic Class Identifier shall not be equal to the Unknown Topic Class Marker.

### 2.2 Actions

- REQ-EMC-2.1: The Below-Threshold Action List and the Above-Threshold Action List shall be lists of texts, where an empty list means no action.
- REQ-EMC-2.2: Each action entry shall be a Mail Tool Command Entry or a Semantic Instruction Entry.
- REQ-EMC-2.3: The text of a Mail Tool Command Entry after the word `gmail` shall be the literal arguments of the gmail CLI.
- REQ-EMC-2.4: The only permitted parameter in a Mail Tool Command Entry shall be the Message Identifier Placeholder, replaced by the MESSAGE_ID of the evaluated message.
- REQ-EMC-2.5: The text of a Semantic Instruction Entry after the prefix `prompt: ` shall be a non-empty verbal description of an operation to be performed by a subagent.

### 2.3 Main thread

- REQ-EMC-3.1: The main thread shall not fetch or quote message content.
- REQ-EMC-3.2: The main thread shall ask every question to the user with the `ask_question` tool, providing ready options of which the first carries the prefix `(Recommended)`.
- REQ-EMC-3.3: The main thread shall determine the number of unread inbox messages from the MESSAGE_ID list returned by the gmail CLI.
- REQ-EMC-3.4: When the number of unread messages exceeds 50 and the user has not specified the number of messages to process, the main thread shall ask the user for the scope with the options: 50 newest messages (recommended), 100 newest messages, all messages in batches of 50 per main-thread loop iteration.
- REQ-EMC-3.5: When the user selects all messages, the main thread shall process them in batches of at most 50 messages per loop iteration until the last batch is processed.
- REQ-EMC-3.6: The main thread shall split a batch into groups of 5 to 10 MESSAGE_IDs and pass each group to a separate subagent.
- REQ-EMC-3.7: The prompt for a subagent shall contain only instructions, the MESSAGE_ID list of the group, and the absolute path of the scoring script, without message content or headers.
- REQ-EMC-3.8: The main thread shall record which subagent evaluated which MESSAGE_ID.
- REQ-EMC-3.9: The main thread shall not invoke the scoring script.
- REQ-EMC-3.10: The main thread shall present to the user a summary report with one row for each processed message, containing the MESSAGE_ID, sender and subject, Topic Class Identifier, Importance Calculation, Autonomous Action Threshold, and performed actions.
- REQ-EMC-3.11: The summary report shall contain all execution errors reported by subagents.

### 2.4 Subagent

- REQ-EMC-4.1: A subagent shall fetch the content of each assigned message with the `readonly get` command of the gmail CLI.
- REQ-EMC-4.2: A subagent shall assign each message to a Topic Class from the Topic Database or mark it with the Unknown Topic Class Marker when it matches no Topic Class.
- REQ-EMC-4.3: A subagent shall set the Message Urgency Score to 1.0 when the action deadline falls within 2 days or the message concerns an outage or a blocker.
- REQ-EMC-4.4: A subagent shall set the Message Urgency Score to 0.5 when the action deadline falls later than 2 days and earlier than 14 days from the current date.
- REQ-EMC-4.5: A subagent shall set the Message Urgency Score to 0.2 when the message has no deadline, the deadline falls 14 days or more from the current date, or the information is outdated relative to the current date.
- REQ-EMC-4.6: A subagent shall determine the Content Importance Score as a number in the range 0.0–1.0 according to the Class-Specific Content Scoring Instructions of the assigned Topic Class.
- REQ-EMC-4.7: When the Class-Specific Content Scoring Instructions of the assigned Topic Class are an empty text, a subagent shall determine the Content Importance Score according to the Default Content Scoring Scale.
- REQ-EMC-4.8: A subagent shall not apply the Default Content Scoring Scale when the Class-Specific Content Scoring Instructions of the assigned Topic Class are non-empty.
- REQ-EMC-4.9: A subagent shall itself invoke the scoring script with a JSON list of Message Evaluation Records, each containing the MESSAGE_ID, date, sender, subject, Topic Class Identifier or Unknown Topic Class Marker, Message Urgency Score, Content Importance Score, a one-sentence summary, and the Class Proposals.
- REQ-EMC-4.10: When the scoring script reports a message in the Range Error List, the subagent shall re-evaluate that message and invoke the scoring script again for it.
- REQ-EMC-4.11: A subagent shall perform each entry of the Deferred Semantic Action List returned by the scoring script, either by invoking the gmail CLI or by preparing information for the summary report, as described by the entry.
- REQ-EMC-4.13: A subagent shall return to the main thread a Message Outcome Record for each message, containing the MESSAGE_ID, sender, subject, Topic Class Identifier, Importance Calculation, Mail Tool Command Entry results, Semantic Instruction Entry results, and execution errors.
- REQ-EMC-4.14: A subagent shall report to the main thread as an execution error every Mail Tool Command Entry that ended with an error, every Semantic Instruction Entry it did not perform, and every scoring script error.
- REQ-EMC-4.15: For a message marked with the Unknown Topic Class Marker, a subagent shall return to the main thread 3 Class Proposals, each containing a Topic Class Identifier, Topic Class Name, Topic Class Description, Topic Class Weight, Class-Specific Content Scoring Instructions, Autonomous Action Threshold, Below-Threshold Action List, and Above-Threshold Action List.

### 2.5 Scoring script

- REQ-EMC-5.1: The scoring script shall accept a JSON list of Message Evaluation Records on standard input.
- REQ-EMC-5.2: The scoring script shall read the Topic Class Weight, Autonomous Action Threshold, Below-Threshold Action List, and Above-Threshold Action List from the Topic Database.
- REQ-EMC-5.3: The scoring script shall place in the Range Error List a message whose MESSAGE_ID is not a non-empty text.
- REQ-EMC-5.4: The scoring script shall place in the Range Error List a message whose Topic Class Identifier is neither present in the Topic Database nor equal to the Unknown Topic Class Marker.
- REQ-EMC-5.6: The scoring script shall place in the Range Error List a message whose Content Importance Score is not a number in the range 0.0–1.0.
- REQ-EMC-5.7: The scoring script shall process the valid messages of the list independently of range errors of other messages.
- REQ-EMC-5.8: The scoring script shall not substitute default values for or clamp out-of-range values.
- REQ-EMC-5.9: The scoring script shall compute the Message Importance Score of a valid message as Message Urgency Score + (Topic Class Weight × Content Importance Score).
- REQ-EMC-5.10: When the Message Importance Score is less than or equal to the Autonomous Action Threshold, the scoring script shall select the Below-Threshold Action List.
- REQ-EMC-5.11: When the Message Importance Score is greater than the Autonomous Action Threshold, the scoring script shall select the Above-Threshold Action List.
- REQ-EMC-5.12: The scoring script shall execute each Mail Tool Command Entry of the selected action through the gmail CLI, after replacing the Message Identifier Placeholder with the MESSAGE_ID, without using a shell.
- REQ-EMC-5.13: When a Mail Tool Command Entry ends with an exit code other than 0, the scoring script shall execute the remaining Mail Tool Command Entries and report the exit code and error message in its result.
- REQ-EMC-5.14: The scoring script shall return each Semantic Instruction Entry of the selected action in the Deferred Semantic Action List together with the MESSAGE_ID, without interpreting it.
- REQ-EMC-5.15: The scoring script shall not perform actions for a message marked with the Unknown Topic Class Marker or for a message in the Range Error List.
- REQ-EMC-5.16: The scoring script shall return on standard output a JSON document containing, for each valid message, the Importance Calculation, Autonomous Action Threshold, Processing Mode, and Mail Tool Command Entry results, as well as the Deferred Semantic Action List and the Range Error List.
- REQ-EMC-5.17: The scoring script shall place in the Range Error List a message whose Message Urgency Score is not a number in the range 0.0–1.0 inclusive.

### 2.6 New classes

- REQ-EMC-6.1: For each message marked with the Unknown Topic Class Marker, the main thread shall ask the user to choose a Topic Class from the Class Proposals and to choose the parameters and actions of that Topic Class.
- REQ-EMC-6.2: The main thread shall generate the Mail Tool Command Entries of a new Topic Class from the help output of the gmail CLI.
- REQ-EMC-6.4: After appending a Topic Class, the main thread shall run the Topic Database validation procedure.
- REQ-EMC-6.5: After a successful validation, the main thread shall send the message with the new Topic Class Identifier to the subagent that evaluated it.
- REQ-EMC-6.6: A subagent that receives a message with a new Topic Class Identifier shall invoke the scoring script for it.
- REQ-EMC-6.7: The main thread shall append the approved Topic Class to the Topic Database with the Topic Class Identifier of the approved Class Proposal and all contents required by REQ-EMC-1.3.

### 2.7 Topic database validation

- REQ-EMC-7.1: The skill shall describe the Topic Database validation as a separate procedure run on demand.
- REQ-EMC-7.2: The validation procedure shall run on user request and after every change of the Topic Database made by the skill.
- REQ-EMC-7.3: The validation script shall check the Topic Database against REQ-EMC-1.2, REQ-EMC-1.3, REQ-EMC-1.5, REQ-EMC-1.7, REQ-EMC-1.11, REQ-EMC-1.15, REQ-EMC-2.1, and REQ-EMC-2.2.
- REQ-EMC-7.4: The validation script shall check that the namespace and command of each Mail Tool Command Entry appear in the output of the `help` command of the gmail CLI.
- REQ-EMC-7.5: The validation script shall check that each flag of a Mail Tool Command Entry appears in the `Flags:` or `Global Flags:` section of the help output of that command.
- REQ-EMC-7.6: The validation script shall treat the token following a flag that has a type in the command help output as the value of that flag, not as a positional argument.
- REQ-EMC-7.7: The validation script shall check the number of positional arguments of a Mail Tool Command Entry against the `Usage:` line of the command help output, counting each `[…]` group as exactly 1 required argument and each group ending with `...]` as at least 1 argument.
- REQ-EMC-7.8: The validation script shall report an error for every `{…}` marker in a Mail Tool Command Entry other than the Message Identifier Placeholder.
- REQ-EMC-7.9: The validation script shall report an error for a Semantic Instruction Entry without text after the prefix.
- REQ-EMC-7.10: When the validation detects an error, the validation script shall end with an exit code other than 0 and print the list of detected problems.
- REQ-EMC-7.11: The validation script shall report an error for every Topic Class whose Topic Class Identifier violates REQ-EMC-1.16.

## 3. Non-functional requirements

- REQ-NF-EMC-1.1: The Message Importance Score shall be computed only by a Python script, not by a language model.
- REQ-NF-EMC-1.2: The skill shall comply with the rules of the `skill-creator` skill: description formula, progress checklist, existing-state check step, `Definition of done` section, paths relative to the skill directory, and a `metadata.version` increment on every edit.
- REQ-NF-EMC-1.3: The skill sources shall reside in the directory `~/workspace/opencode-skills/jetski/email-classifier/`.
- REQ-NF-EMC-1.4: The script code shall contain documentation URLs of the library functions it uses.
- REQ-NF-EMC-1.5: Public functions of the scripts shall check the type and range of their arguments, and the remaining code shall not contain defensive coding.
- REQ-NF-EMC-1.6: All identifiers in the skill files, including keys of JSON documents, shall be English.
- REQ-NF-EMC-1.7: Comments, documentation strings, and messages of the scripts shall be English.

## 4. Decided exclusions

- Topic Classes shall not contain textual action notes; the Mail Tool Command Entry is a sufficient description of intent (user decision 2026-10-29).
- The scoring script shall not interpret the text of Semantic Instruction Entries (user decision 2026-10-29).
- Requirements shall not prescribe identifiers used in code or data; identifiers are a design decision (user decision 2026-10-29).

## 5. Requirement provenance

| Requirement ID | Source or parent | Rationale | Decision authority |
|---|---|---|---|
| REQ-EMC-1.1 | User decision 2026-10-29 | Text table replaced by JSON; location chosen by the user. | User |
| REQ-EMC-1.2 | User decision 2026-10-29 (approved JSON template) | Approved template format. | User |
| REQ-EMC-1.3 | User decisions 2026-10-26 to 2026-10-29 | Contents follow from the scoring model, actions, and class instructions. | User |
| REQ-EMC-1.5 | User decision 2026-10-27 | Class weight in the range 0–1. | User |
| REQ-EMC-1.7 | User decision 2026-10-29 | Empty class instructions enable the default scale. | User |
| REQ-EMC-1.8 | User decision 2026-10-26 | Topics must be very generic. | User |
| REQ-EMC-1.11 | User decision 2026-10-29, REQ-EMC-1.5, REQ-EMC-5.17 | Full attainable Message Importance Score range 0.00–2.00. | User |
| REQ-EMC-1.12 | User decision 2026-10-29 | A new database is built from the user's decisions through the new class procedure. | User |
| REQ-EMC-1.13 | User decision 2026-10-29 | The template is not a default database. | User |
| REQ-EMC-1.14 | User decision 2026-10-29 | Examples are kept separate from the template and outside the skill instructions. | User |
| REQ-EMC-1.15 | User decision 2026-10-29 | Semantic identifiers such as `CODE_REVIEW` are permitted alongside numbered ones. | User |
| REQ-EMC-1.16 | User decision 2026-10-29 | A class with the marker as identifier would never be selected by the scoring script. | User |
| REQ-EMC-2.1 | User decision 2026-10-29 | Multiple entries per action; empty list means no action. | User |
| REQ-EMC-2.2 | User decision 2026-10-29 | Two entry kinds. | User |
| REQ-EMC-2.3 | User decision 2026-10-29 | Commands are gmail CLI arguments. | User |
| REQ-EMC-2.4 | User decision 2026-10-29 | The only parameter is the Message Identifier Placeholder. | User |
| REQ-EMC-2.5 | User decision 2026-10-29 | A Semantic Instruction Entry describes an operation verbally. | User |
| REQ-EMC-3.1 | User decision 2026-10-27 | The main thread does not process message content. | User |
| REQ-EMC-3.2 | User decision 2026-10-27 | Questions only through the tool, with ready options. | User |
| REQ-EMC-3.3 | User decision 2026-10-27 | Message count check at start. | User |
| REQ-EMC-3.4 | User decision 2026-10-27 (SKILL.md edit by the user) | Limit of 50 and question options. | User |
| REQ-EMC-3.5 | REQ-EMC-3.4 | The "all" option requires a loop over batches. | User |
| REQ-EMC-3.6 | Plan approved by the user 2026-10-29 | Work distribution across subagents. | User |
| REQ-EMC-3.7 | User decision 2026-10-27, plan approved 2026-10-29 | Self-contained prompt without quoting messages; the subagent needs the script path. | User |
| REQ-EMC-3.8 | REQ-EMC-6.5 | Returning a message to the same subagent requires the assignment. | User |
| REQ-EMC-3.9 | User decision 2026-10-29 | Subagents invoke the script. | User |
| REQ-EMC-3.10 | User decision 2026-10-27 | Report with calculation and action. | User |
| REQ-EMC-3.11 | User decision 2026-10-29 | Execution errors must reach the user. | User |
| REQ-EMC-4.1 | User decision 2026-10-27 | The subagent fetches message content itself. | User |
| REQ-EMC-4.2 | User decision 2026-10-26 | Classification or missing-class signal. | User |
| REQ-EMC-4.3 | User decisions 2026-10-26 and 2026-10-29 | Urgent: within 2 days, value 1.0; the subagent keeps discrete values. | User |
| REQ-EMC-4.4 | User decisions 2026-10-26 and 2026-10-29 | Medium urgency: later than 2 days and earlier than 14 days, value 0.5. | User |
| REQ-EMC-4.5 | User decisions 2026-10-26, 2026-10-27, and 2026-10-29 | Not urgent: 14 days or more, no deadline, or outdated, value 0.2. | User |
| REQ-EMC-4.6 | User decision 2026-10-27 | Individual scoring instructions per class. | User |
| REQ-EMC-4.7 | User decision 2026-10-29 | The default scale applies only to empty class instructions. | User |
| REQ-EMC-4.8 | User decision 2026-10-29 | The default scale does not apply in any other case. | User |
| REQ-EMC-4.9 | User decision 2026-10-29 | The subagent invokes the script itself; contents from the approved format. | User |
| REQ-EMC-4.10 | User decisions 2026-10-29 | A range error requires re-evaluation by the evaluator. | User |
| REQ-EMC-4.11 | User decision 2026-10-29 | The subagent performs Semantic Instruction Entries itself. | User |
| REQ-EMC-4.13 | User decision 2026-10-29 | Results for the summary report. | User |
| REQ-EMC-4.14 | User decision 2026-10-29 | Execution errors reported to the user. | User |
| REQ-EMC-4.15 | User decisions 2026-10-27 and 2026-10-29, REQ-EMC-1.3 | Ready proposals for confirmation, including a semantic identifier. | User |
| REQ-EMC-5.1 | User decision 2026-10-27 | The script accepts the aggregated list. | User |
| REQ-EMC-5.2 | User decision 2026-10-27 | Calculation according to the class file. | User |
| REQ-EMC-5.3 | User decision 2026-10-29 | Range error instead of default values. | User |
| REQ-EMC-5.4 | User decision 2026-10-29 | Range error instead of default values. | User |
| REQ-EMC-5.6 | User decision 2026-10-29 | Range error instead of default values. | User |
| REQ-EMC-5.7 | User decision 2026-10-29 | An error affects only the faulty items. | User |
| REQ-EMC-5.8 | User decision 2026-10-29, user global rules | No defensive coding. | User |
| REQ-EMC-5.9 | User decision 2026-10-27 | Importance formula. | User |
| REQ-EMC-5.10 | User decision 2026-10-27 | Autonomous action up to and including the threshold. | User |
| REQ-EMC-5.11 | User decision 2026-10-27 | Action above the threshold. | User |
| REQ-EMC-5.12 | User decisions 2026-10-29 | The script executes Mail Tool Command Entries itself. | User |
| REQ-EMC-5.13 | User decision 2026-10-29 | One error does not block the rest. | User |
| REQ-EMC-5.14 | User decision 2026-10-29 | Semantic Instruction Entries returned in a special list. | User |
| REQ-EMC-5.15 | REQ-EMC-5.3, REQ-EMC-5.4, REQ-EMC-5.6, REQ-EMC-5.17, REQ-EMC-6.1 | Missing class or invalid data prevents action selection. | User |
| REQ-EMC-5.16 | User decisions 2026-10-27 to 2026-10-29 | Result as JSON on standard output. | User |
| REQ-EMC-5.17 | User decision 2026-10-29 | The script accepts a continuous urgency range. | User |
| REQ-EMC-6.1 | User decision 2026-10-27 | New class through a question with ready proposals. | User |
| REQ-EMC-6.2 | User decision 2026-10-29 | Commands generated from the gmail CLI help output. | User |
| REQ-EMC-6.4 | User decision 2026-10-29 | Validation after every database change. | User |
| REQ-EMC-6.5 | User decision 2026-10-29 | Returning the message to the same subagent. | User |
| REQ-EMC-6.6 | User decision 2026-10-29 | The subagent invokes the script. | User |
| REQ-EMC-6.7 | User decision 2026-10-29 | New classes receive the semantic identifier from the approved proposal. | User |
| REQ-EMC-7.1 | User decision 2026-10-29 | Validation as a separate on-demand procedure. | User |
| REQ-EMC-7.2 | User decision 2026-10-29 | Validation triggers. | User |
| REQ-EMC-7.3 | REQ-EMC-1.2, REQ-EMC-1.3, REQ-EMC-1.5, REQ-EMC-1.7, REQ-EMC-1.11, REQ-EMC-1.15, REQ-EMC-2.1, REQ-EMC-2.2 | Database structure check. | User |
| REQ-EMC-7.4 | User decision 2026-10-29 | Comparison with available gmail CLI commands. | User |
| REQ-EMC-7.5 | User decision 2026-10-29 | Comparison with command options. | User |
| REQ-EMC-7.6 | REQ-EMC-7.5, REQ-EMC-7.7 | Correct separation of flag values from positional arguments. | User |
| REQ-EMC-7.7 | User decision 2026-10-29 (rule A) | Strict argument counting rule. | User |
| REQ-EMC-7.8 | REQ-EMC-2.4 | The only permitted parameter. | User |
| REQ-EMC-7.9 | REQ-EMC-2.5 | A Semantic Instruction Entry must have a description. | User |
| REQ-EMC-7.10 | User decision 2026-10-29 | Validation result visible to the caller. | User |
| REQ-EMC-7.11 | REQ-EMC-1.16 | Reserved identifier check. | User |
| REQ-NF-EMC-1.1 | User decision 2026-10-29 | Precise arithmetic in Jetski is available only in Python. | User |
| REQ-NF-EMC-1.2 | User instruction 2026-10-29 (use of the skill-creator skill) | Compliance with skill authoring guidance. | User |
| REQ-NF-EMC-1.3 | User decision 2026-10-29 | Location in the repository. | User |
| REQ-NF-EMC-1.4 | User global rules | Prohibition of undocumented APIs. | User |
| REQ-NF-EMC-1.5 | User global rules | Coding style. | User |
| REQ-NF-EMC-1.6 | User decision 2026-10-29 | English identifiers in all files. | User |
| REQ-NF-EMC-1.7 | User decision 2026-10-29 | No Polish language in scripts. | User |

## 6. Requirement lifecycle map

| Previous ID | Disposition | Successor | Reason |
|---|---|---|---|
| REQ-EMC-1.6 | Replaced | REQ-EMC-1.11 | Threshold range widened from 0.20–2.00 to 0.00–2.00 after the continuous urgency decision (user decision 2026-10-29). |
| REQ-EMC-5.5 | Replaced | REQ-EMC-5.17 | Scoring script accepts a continuous urgency range 0.0–1.0 instead of the values 0.2, 0.5, 1.0 (user decision 2026-10-29). |
| REQ-EMC-1.9 | Replaced | REQ-EMC-1.12 | A missing Topic Database is created with an empty Topic Class Collection instead of a copy of default classes (user decision 2026-10-29). |
| REQ-EMC-1.4 | Replaced | REQ-EMC-1.15 | Identifier format widened from `TOPIC-<number>` to uppercase letters, digits, underscores, and hyphens without spaces (user decision 2026-10-29). |
| REQ-EMC-4.12 | Replaced | REQ-EMC-4.15 | Class Proposals additionally contain a proposed Topic Class Identifier (user decision 2026-10-29). |
| REQ-EMC-6.3 | Replaced | REQ-EMC-6.7 | New classes receive the identifier of the approved proposal instead of the next `TOPIC-<number>` (user decision 2026-10-29). |
| REQ-EMC-1.10 | Replaced | REQ-EMC-1.13 | The Database Template is empty and is not a default database (user decision 2026-10-29). |
| REQ-EMC-1.2 | Clarified | REQ-EMC-1.2 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-1.3 | Clarified | REQ-EMC-1.3 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-1.5 | Clarified | REQ-EMC-1.5 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-1.7 | Clarified | REQ-EMC-1.7 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-2.1 | Clarified | REQ-EMC-2.1 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-2.2 | Clarified | REQ-EMC-2.2 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-2.4 | Clarified | REQ-EMC-2.4 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-3.10 | Clarified | REQ-EMC-3.10 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.2 | Clarified | REQ-EMC-4.2 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.3 | Clarified | REQ-EMC-4.3 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.4 | Clarified | REQ-EMC-4.4 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.5 | Clarified | REQ-EMC-4.5 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.6 | Clarified | REQ-EMC-4.6 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.7 | Clarified | REQ-EMC-4.7 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.8 | Clarified | REQ-EMC-4.8 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.9 | Clarified | REQ-EMC-4.9 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.10 | Clarified | REQ-EMC-4.10 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.11 | Clarified | REQ-EMC-4.11 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.13 | Clarified | REQ-EMC-4.13 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-4.14 | Clarified | REQ-EMC-4.14 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.2 | Clarified | REQ-EMC-5.2 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.3 | Clarified | REQ-EMC-5.3 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.4 | Clarified | REQ-EMC-5.4 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.6 | Clarified | REQ-EMC-5.6 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.9 | Clarified | REQ-EMC-5.9 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.10 | Clarified | REQ-EMC-5.10 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.11 | Clarified | REQ-EMC-5.11 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.12 | Clarified | REQ-EMC-5.12 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.13 | Clarified | REQ-EMC-5.13 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.14 | Clarified | REQ-EMC-5.14 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.15 | Clarified | REQ-EMC-5.15 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-5.16 | Clarified | REQ-EMC-5.16 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-6.1 | Clarified | REQ-EMC-6.1 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-6.2 | Clarified | REQ-EMC-6.2 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-6.5 | Clarified | REQ-EMC-6.5 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-6.6 | Clarified | REQ-EMC-6.6 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-7.3 | Clarified | REQ-EMC-7.3 | References updated to successor REQ-EMC-1.11 (user decision 2026-10-29). |
| REQ-EMC-7.4 | Clarified | REQ-EMC-7.4 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-7.5 | Clarified | REQ-EMC-7.5 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-7.7 | Clarified | REQ-EMC-7.7 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-7.8 | Clarified | REQ-EMC-7.8 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |
| REQ-EMC-7.9 | Clarified | REQ-EMC-7.9 | Implementation identifiers replaced by defined code names (user decision 2026-10-29). |

# Library Management Testing Documentation

## Test Case 1.1: Create New Member

**Objective**: Verify that a new library member can be created successfully with all required fields.

**Prerequisites**:

* ERPNext/Frappe is running
* Library Management app is installed

**Steps**:

1. Navigate to Library Member.
2. Click New.
3. Fill all required fields.
4. Click Save.

**Expected Result**:

* Member saves successfully.
* Member ID is auto-generated.
* Member appears in list view.

**Actual Result**:

* Member saved successfully.
* Member ID generated correctly.
* Member visible in list view.

**Status**: ✅ Pass

**Screenshot**: screenshots/member_create.png

---

## Test Case 1.2: Edit Member Details

**Objective**: Verify member details can be updated.

**Prerequisites**:

* Existing member record available.

**Steps**:

1. Open an existing member.
2. Change Membership Type.
3. Save.

**Expected Result**:

* Changes persist after save.

**Actual Result**:

* Membership Type updated successfully.

**Status**: ✅ Pass

**Screenshot**: screenshots/member_edit.png

---

## Test Case 1.3: Email Uniqueness

**Objective**: Verify duplicate email addresses are not allowed.

**Prerequisites**:

* Existing member with registered email.

**Steps**:

1. Create a new member.
2. Enter an existing email address.
3. Save.

**Expected Result**:

* Validation error appears.

**Actual Result**:

* Duplicate email prevented.

**Status**: ✅ Pass

**Screenshot**: screenshots/member_email_unique.png

---

## Test Case 1.4: Member Status Change

**Objective**: Verify member status updates correctly.

**Prerequisites**:

* Existing member record.

**Steps**:

1. Open member.
2. Change Status from Active to Inactive.
3. Saved.

**Expected Result**:

* Status saved.

**Actual Result**:

* Status changed successfully.

**Status**: ✅ Pass

**Screenshot**: screenshots/member_status_change.png

---

## Test Case 1.5: Delete Member

**Objective**: Verify member deletion functionality.

**Prerequisites**:

* Test member exists.

**Steps**:

1. Open member.
2. Delete record.
3. Confirm deletion.

**Expected Result**:

* Member removed from list.

**Actual Result**:

* Member deleted successfully.

**Status**: ✅ Pass

**Screenshot**: screenshots/member_delete.png

---

# Section 2: Book Tests

## Test Case 2.1: Create New Book

**Objective**: Verify a new book can be created successfully.

**Prerequisites**:

* Book DocType exists.

**Steps**:

1. Create a new book.
2. Fill all required fields.
3. Save.

**Expected Result**:

* Book saves successfully.
* Book ID auto-generated.
* Available Copies equals Total Copies.

**Actual Result**:

* Book created successfully.

**Status**: ✅ Pass

**Screenshot**: screenshots/book_created.png

---

## Test Case 2.2: Available Copies Auto-Set

**Objective**: Verify available copies automatically equal total copies.

**Prerequisites**:

* Book DocType exists.

**Steps**:

1. Create a book with Total Copies = 5.
2. Save.

**Expected Result**:

* Available Copies automatically set to 5.

**Actual Result**:

* Available Copies still showing same is earliear enter.

**Status**: failed

**Screenshot**: screenshots/available_copies_auto.png

---

## Test Case 2.3: Edit Total Copies

**Objective**: Verify available copies do not exceed total copies.

**Prerequisites**:

* Existing book record.

**Steps**:

1. Open a book.
2. Change Total Copies from 5 to 3.
3. Save.

**Expected Result**:

* Available Copies adjusted accordingly.

**Actual Result**:

* Available Copies updated correctly.

**Status**: ✅ Pass

**Screenshot**: screenshots/edit_total_copies.png

---

## Test Case 2.4: Negative Copies Validation

**Objective**: Verify negative values are not allowed.

**Prerequisites**:

* Book DocType exists.

**Steps**:

1. Set Total Copies = -1.
2. Save.

**Expected Result**:

* Validation error displayed.

**Actual Result**:

* Save prevented with error message.

**Status**: ✅ Pass

**Screenshot**: screenshots/negative_copies_validation.png

---

## Test Case 2.5: ISBN Uniqueness

**Objective**: Verify duplicate ISBN numbers are not allowed.

**Prerequisites**:

* Existing book with ISBN.

**Steps**:

1. Create another book.
2. Use same ISBN.
3. Save.

**Expected Result**:

* Validation error displayed.

**Actual Result**:

* Duplicate ISBN prevented.

**Status**: ✅ Pass

**Screenshot**: screenshots/isbn_unique_validation.png

---

# Section 3: Book Transaction Tests

## Test Case 3.1: Create Issue Transaction

**Objective**: Verify Issue transactions can be created successfully.

**Prerequisites**:

* At least one Member exists.
* At least one Book exists.

**Steps**:

1. Create Book Transaction.
2. Select Member.
3. Select Book.
4. Select Transaction Type = Issue.
5. Enter Due Date.
6. Save.

**Expected Result**:

* Transaction saved successfully.

**Actual Result**:

* Issue transaction created.

**Status**: ✅ Pass

**Screenshot**: screenshots/issue_transaction.png

---

## Test Case 3.2: Issue Without Due Date

**Objective**: Verify Due Date is mandatory for Issue transactions.

**Prerequisites**:

* Book Transaction DocType exists.

**Steps**:

1. Create Issue transaction.
2. Leave Due Date blank.
3. Save.

**Expected Result**:

* Validation error displayed.

**Actual Result**:

* Save prevented with validation message.

**Status**: ✅ Pass

**Screenshot**: screenshots/issue_without_due_date.png

---

## Test Case 3.3: Create Return Transaction

**Objective**: Verify Return transactions can be created successfully.

**Prerequisites**:

* Existing Member and Book.

**Steps**:

1. Create transaction.
2. Select Return.
3. Enter Return Date.
4. Save.

**Expected Result**:

* Transaction saved successfully.

**Actual Result**:

* Return transaction created.

**Status**: ✅ Pass

**Screenshot**: screenshots/return_transaction.png

---

## Test Case 3.4: Return Without Return Date

**Objective**: Verify Return Date is mandatory.

**Prerequisites**:

* Book Transaction DocType exists.

**Steps**:

1. Create Return transaction.
2. Leave Return Date blank.
3. Save.

**Expected Result**:

* Validation error displayed.

**Actual Result**:

* Save prevented.

**Status**: ✅ Pass

**Screenshot**: screenshots/return_without_return_date.png

---

## Test Case 3.5: Invalid Return Date

**Objective**: Verify Return Date cannot be before Transaction Date.

**Prerequisites**:

* Book Transaction DocType exists.

**Steps**:

1. Create Return transaction.
2. Set Return Date before Transaction Date.
3. Save.

**Expected Result**:

* Validation error displayed.

**Actual Result**:

* Save prevented.

**Status**: ✅ Pass

**Screenshot**: screenshots/invalid_return_date.png

---

# Section 4: Integration Tests

## Test Case 4.1: Complete Checkout Flow

**Objective**: Verify complete library workflow.

**Prerequisites**:

* Application setup completed.

**Steps**:

1. Create Member.
2. Create Book.
3. Create Issue Transaction.
4. Verify records.

**Expected Result**:

* Complete flow works successfully.

**Actual Result**:

* Member, Book and Transaction linked correctly.

**Status**: ✅ Pass

**Screenshot**: screenshots/complete_checkout_flow.png

---

## Test Case 4.2: Link Field Functionality

**Objective**: Verify Link fields work correctly.

**Prerequisites**:

* Members and Books already exist.

**Steps**:

1. Open Book Transaction.
2. Click Member field.
3. Select a member.
4. Click Book field.
5. Select a book.

**Expected Result**:

* Link fields display available records and populate correctly.

**Actual Result**:

* Link fields functioned as expected.

**Status**: ✅ Pass

**Screenshot**: screenshots/link_field_functionality.png

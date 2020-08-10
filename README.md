# Flatten This

How much wood would a woodchuck chuck if a woodchuck could chuck wood?

Our analysts want to answer this question in an objective way, so they've
gathered a lot of data about woodchucks that they intend to crunch through
with SQL.

The problem is that the data they got is in JSON, and a lot of it is
not flat.

For example:

```json
{
    "name": "Cap'n Chuck",
    "aliases": ["Chuck Force 1", "Whistlepig"],
    "physical": {
        "height_in": 26,
        "weight_lb": 18
    },
    "wood_chucked_lbs": 2281
}
```

How do you load JSON like this into a regular database table so you can
query it with SQL? Our Chief Woodchuck Scientist has proposed flattening
the data to make this possible.

For example, Cap'n Chuck's record would be flattened as follows:

```json
{
    "name": "Cap'n Chuck",
    "aliases.0": "Chuck Force 1",
    "aliases.1": "Whistlepig",
    "physical.height_in": 26,
    "physical.weight_lb": 18,
    "wood_chucked_lbs": 2281
}
```

"These flattened fields can now be mapped to columns in a table and queried
with SQL. It's genius!" exclaims our Chief Woodchuck Scientist.

Pop open `flatten.py` and implement the stubbed-out flattening function
so our analysts can flatten their data and answer this age-old question.

## Evaluation Guidelines

Your answer will be graded based on the following criteria:

* Correctness: Does your answer work? How can you demonstrate that it
               does?
* Robustness: Does your answer cover edge cases and fail gracefully?
* Legibility: Is your answer easy for others to read and understand?
* Coding Style: Does your answer follow common coding conventions?

## Follow-up Email

Team Woodchuck is ready to charge ahead and build their first analytics
product on this basic architecture. Do you see any potential problems with
the approach they're taking? Is there an alternative way of tackling the
problem that they should consider?

Write a brief email to the team laying out your thoughts. You can edit it
in here.

------------------------------------------------------------------------

Hey Team,

We're currently focused on building our woodchucks analytics tool.

A lot of data is coming from JSON files and using `flatten.py` module
in the attachment we can save and map the data in our SQL database
for later analysis.

How do we ensure we correctly map this data?

- JSON documents should have normalized keys
    "wood_chucked_lbs"
    "wood chucked lbs"
    "wood_CHUCKED lbs"

- values in JSON documents must be validated
    "wood_chucked_lbs": "<an_actual_number>"

- JSON documents have an unspecified number of attributes. because of this
  partitioned data would yield better performance.

  Given this flattened JSON:

    {
        "name": "Cap'n Chuck",
        "aliases.0": "Chuck Force 1",
        "aliases.1": "Whistlepig",
        "physical.height_in": 26,
        "physical.weight_lb": 18,
        "wood_chucked_lbs": 2281
    }

    partition by first unflattened dict key

    table 1 - name attribute
    table 2 - aliases.0, aliases.1
    table 3 - physical.height_in, physical.weight_lb
    etc.

    This has some advantages when querying with SQL
    like skipping physical attributes and not join that
    table if it is not needed in the analytics report.

- change database to columnar database?

Can we have a discussion/meeting about this?


Best regards,
Razvan


------------------------------------------------------------------------

## Feedback

When you're done with everything, answer the following questions. We use
this feedback to tune the exercise and give you an opportunity to add any
extra thoughts you may have.

You can edit your answers in here.

1. How long did the programming exercise take you to complete? How about
   the email?

    - code programming exercise took about an hour and a half.
    - email 30 minutes because writing email is hard.

2. Any comments on the whole exercise process itself, or on any of your
   answers?

    - it's better than an online timed algorithm problem and feels more
      like a real-world issue.

from datetime import datetime
from typing import Any, Dict

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    SubmitField,
    StringField,
    TelField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Optional


class SignUpForm(FlaskForm):
    customer_name = StringField(
        "Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Daphne Blake", "class": "u-full-width"},
    )

    customer_phone = TelField(
        "Phone",
        validators=[DataRequired()],
        render_kw={"placeholder": "(+44) 0123 456789", "class": "u-full-width"},
    )

    customer_email = StringField(
        "Email",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "daphne@themysterymachine.com",
            "class": "u-full-width",
        },
    )

    customer_emergency_contact_name = StringField(
        "Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Fred Jones", "class": "u-full-width"},
    )

    customer_emergency_contact_phone = TelField(
        "Phone",
        validators=[DataRequired()],
        render_kw={"placeholder": "(+44) 1234 567890", "class": "u-full-width"},
    )

    customer_signed_up_on = DateField("customer_signed_up_on", default=datetime.utcnow)

    vet_name = StringField(
        "Vet",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Enter the name of your dog's vet",
            "class": "u-full-width",
        },
    )

    other_vet_name = StringField("Other Vet")

    dog_name = StringField(
        "Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Scooby Doo", "class": "u-full-width"},
    )

    dog_breed = StringField(
        "Breed",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Enter the breed of your dog",
            "class": "u-full-width",
        },
    )
    other_dog_breed = StringField(
        "Other Dog Breed",
        render_kw={
            "placeholder": "Enter other dog breed",
            "class": "u-full-width",
        },
    )

    dog_date_of_birth = DateField(
        "Date of Birth",
        validators=[Optional()],
        render_kw={"class": "u-full-width"},
    )

    dog_is_allowed_treats = BooleanField(
        "Allowed treats?",
        default=False,
    )

    dog_is_allowed_off_the_lead = BooleanField(
        "Allowed off the lead?",
        default=False,
    )

    dog_is_allowed_on_social_media = BooleanField(
        "Allowed on Instagram (@w4lkies) or this website (w4lkies.com)?",
        default=False,
    )

    dog_is_neutered_or_spayed = BooleanField("Neutered or spayed?", default=False)

    dog_behavioral_issues = TextAreaField(
        "Behavioral Issues",
        validators=[Optional()],
        render_kw={
            "placeholder": "Enter any behavior issues your dog may have",
            "class": "u-full-width",
        },
    )

    dog_medical_needs = TextAreaField(
        "Medical Needs / Allergies",
        validators=[Optional()],
        render_kw={
            "placeholder": "Enter any information about your dog's medical needs or allergies",
            "class": "u-full-width",
        },
    )

    consent = BooleanField(
        f"""
        "I authorize W4lkies Ltd to care for my dog(s) in my absence and to transport them to a veterinary clinic for medical treatment if necessary. I understand that I will be responsible for payment for any treatment provided to my dog(s) by W4lkies Ltd or the veterinary clinic. In the event that W4lkies Ltd is unable to contact me or my emergency contact, I authorize W4lkies Ltd and the veterinary clinic to make any necessary decisions regarding my dog(s) medical treatment."
        """,
        validators=[DataRequired()],
    )

    submit = SubmitField("Submit")

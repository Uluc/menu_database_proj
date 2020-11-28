from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100, default="United States")

    class State(models.TextChoices):
        ALABAMA = "AL"
        ALASKA = "AK"
        ARIZONA = "AZ"
        ARKANSAS = "AR"
        CALIFORNIA = "CA"
        COLORADO = "CO"
        CONNECTICUT = "CT"
        DELAWARE = "DE"
        FLORIDA = "FL"
        GEORGIA = "GA"
        HAWAII = "HI"
        IDAHO = "ID"
        ILLINOIS = "IL"
        INDIANA = "IN"
        IOWA = "IA"
        KANSAS = "KS"
        KENTUCKY = "KY"
        LOUISIANA = "LA"
        MAINE = "ME"
        MARYLAND = "MD"
        MASSACHUSETTS = "MA"
        MICHIGAN = "MI"
        MINNESOTA = "MN"
        MISSISSIPPI = "MS"
        MISSOURI = "MO"
        MONTANA = "MT"
        NEBRASKA = "NE"
        NEVADA = "NV"
        NEWHAMPSHIRE = "NH"
        NEWJERSEY = "NJ"
        NEWMEXICO = "NM"
        NEWYORK = "NY"
        NORTHCAROLINA = "NC"
        NORTHDAKOTA = "ND"
        OHIO = "OH"
        OKLAHOMA = "OK"
        OREGON = "OR"
        PENNSYLVANIA = "PA"
        RHODEISLAND = "RI"
        SOUTHCAROLINA = "SC"
        SOUTHDAKOTA = "SD"
        TENNESSEE = "TN"
        TEXAS = "TX"
        UTAH = "UT"
        VERMONT = "VT"
        VIRGINIA = "VA"
        WASHINGTON = "WA"
        WESTVIRGINIA = "WV"
        WISCONSIN = "WI"
        WYOMING = "WY"

    state = models.CharField(max_length=2, choices=State.choices)

    city = models.CharField(max_length=85, default="Baton Rouge")
    county = models.CharField(max_length=50, default="East Baton Rouge")
    street_address = models.CharField(max_length=50)
    zipcode = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    
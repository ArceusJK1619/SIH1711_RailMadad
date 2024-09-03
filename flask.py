from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import string

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

# Demo data creation

# Train routes and Route In-Charges
routes = {
    "Route 1": "Delhi to Mumbai",
    "Route 2": "Chennai to Kolkata",
    "Route 3": "Bangalore to Hyderabad",
    "Route 4": "Jaipur to Pune",
    "Route 5": "Ahmedabad to Surat"
}

route_incharges = {
    "RouteInCharge1": {"id": "RIC1", "password": "password1", "routes": ["Route 1"]},
    "RouteInCharge2": {"id": "RIC2", "password": "password2", "routes": ["Route 2"]},
    "RouteInCharge3": {"id": "RIC3", "password": "password3", "routes": ["Route 3"]},
    "RouteInCharge4": {"id": "RIC4", "password": "password4", "routes": ["Route 4"]},
    "RouteInCharge5": {"id": "RIC5", "password": "password5", "routes": ["Route 5"]}
}

# TTEs assignment
ttes = {
    "Route 1": [
        {"id": "TTE1", "password": "ttepass1", "half": "first"},
        {"id": "TTE2", "password": "ttepass2", "half": "second"}
    ],
    "Route 2": [
        {"id": "TTE3", "password": "ttepass3", "half": "first"},
        {"id": "TTE4", "password": "ttepass4", "half": "second"}
    ],
    "Route 3": [
        {"id": "TTE5", "password": "ttepass5", "half": "first"},
        {"id": "TTE6", "password": "ttepass6", "half": "second"}
    ],
    "Route 4": [
        {"id": "TTE7", "password": "ttepass7", "half": "first"},
        {"id": "TTE8", "password": "ttepass8", "half": "second"}
    ],
    "Route 5": [
        {"id": "TTE9", "password": "ttepass9", "half": "first"},
        {"id": "TTE10", "password": "ttepass10", "half": "second"}
    ]
}

# CRPF personnel assignment
crpfs = {
    "Route 1": [
        {"id": "CRPF1", "password": "crpfpass1", "half": "first"},
        {"id": "CRPF2", "password": "crpfpass2", "half": "first"},
        {"id": "CRPF3", "password": "crpfpass3", "half": "second"},
        {"id": "CRPF4", "password": "crpfpass4", "half": "second"}
    ],
    "Route 2": [
        {"id": "CRPF5", "password": "crpfpass5", "half": "first"},
        {"id": "CRPF6", "password": "crpfpass6", "half": "first"},
        {"id": "CRPF7", "password": "crpfpass7", "half": "second"},
        {"id": "CRPF8", "password": "crpfpass8", "half": "second"}
    ],
    "Route 3": [
        {"id": "CRPF9", "password": "crpfpass9", "half": "first"},
        {"id": "CRPF10", "password": "crpfpass10", "half": "first"},
        {"id": "CRPF11", "password": "crpfpass11", "half": "second"},
        {"id": "CRPF12", "password": "crpfpass12", "half": "second"}
    ],
    "Route 4": [
        {"id": "CRPF13", "password": "crpfpass13", "half": "first"},
        {"id": "CRPF14", "password": "crpfpass14", "half": "first"},
        {"id": "CRPF15", "password": "crpfpass15", "half": "second"},
        {"id": "CRPF16", "password": "crpfpass16", "half": "second"}
    ],
    "Route 5": [
        {"id": "CRPF17", "password": "crpfpass17", "half": "first"},
        {"id": "CRPF18", "password": "crpfpass18", "half": "first"},
        {"id": "CRPF19", "password": "crpfpass19", "half": "second"},
        {"id": "CRPF20", "password": "crpfpass20", "half": "second"}
    ]
}

# Generate random PNR numbers for each route
pnrs = {
    route: ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    for route in routes
}

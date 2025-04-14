from datetime import datetime, timedelta
import os

from flask import Blueprint, redirect, render_template, send_from_directory

legal_bp = Blueprint("legal_bp", __name__)


@legal_bp.route("/", methods=["GET"])
def get():
    return render_template("legal.html"), 200

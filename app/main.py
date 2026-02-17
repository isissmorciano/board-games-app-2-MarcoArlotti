from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template()

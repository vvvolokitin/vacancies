from flask import Blueprint, render_template

from .dao.candidates_dao import CandidateDAO

candidates_dao = CandidateDAO('./data/candidates.json')

candidates_blueprint: Blueprint = Blueprint(
    'candidates_blueprint',
    __name__,
    url_prefix='/candidates',
    template_folder='templates'
)


@candidates_blueprint.route('/')
def page_candidates_all() -> str:
    """
    Возвращает страницу со всеми кандидатами.

    Возвращаемое значение:
        str: Информация о всех кандидатах.
    """
    candidates = candidates_dao.get_all()
    return render_template('candidates_index.html', candidates=candidates)


@candidates_blueprint.route('/<int: pk>')
def page_candidate(pk) -> str:
    """
    Возвращает страницу с однимкандидатом.

    Возвращаемое значение:
        str: Информация о кандидате.
    """
    candidate = candidates_dao.get_by_pk(pk)
    return render_template('candidates_single.html', candidate=candidate)

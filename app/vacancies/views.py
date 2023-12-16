from flask import Blueprint, render_template

from .dao.vacancies_dao import VacanciesDAO


vacancies_blueprint: Blueprint = Blueprint(
    'vacancies_blueprint',
    __name__,
    template_folder='templates'
)

vacancies_dao = VacanciesDAO('./data/vacancies.json')


@vacancies_blueprint.route('/vacancies/')
def page_vacancies():
    """
    Возвращает страницу со всеми вакансиями.

    Возвращаемое значение:
        str: Информация о всех вакансиях.
    """
    vacancies = vacancies_dao.get_all()
    return render_template('vacancies_index.html', vacancies=vacancies)


@vacancies_blueprint.route('/vacancies/<int:pk>')
def page_vacancies_single(pk) -> str:
    """
    Возвращает страницу с одной вакансией.

    Возвращаемое значение:
        str: Информация о вакансии.
    """
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template('vacancies_single.html', vacancy=vacancy)

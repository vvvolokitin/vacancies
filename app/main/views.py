from flask import Blueprint


main_blueprint: Blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def page_index() -> str:
    """
   Возвращает главную страницу.

   Возвращаемое значение:
       str: главная страница сайта.
   """
    return 'Это главная страница'

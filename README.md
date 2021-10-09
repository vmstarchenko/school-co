# school-co

План (бэк):
- [X] (.5) Инициализировать структуру директорий проекта (etc, var, server, ...)
- [X] (1) Инициализировать простой сервер через докер и инициализировать основное приложение
- [ ] (3) Добавить модельки:
  - "учебное заведение"
	  - название (название школы в которой учится ученик)
  - "ученик"
	  - ФИО
		- класс
		- УчебноеЗаведение
		- жанр
		- регион
  - "ученический текст"
	  - текст
		- скан (будет добавлено как позже как ссылка на модель файлов)
		- статус (не размеченный, размеченный)
  - "аннотация"
		- УчебныйТекст
	  - offset начала аннотации
		- offset окончания аннотации
		- иcправление аннотации (текст с правильный вариантом. Если в изначальном тексте подстроку [offset_begin:offset_end] заменить на исправление, то должен получиться корректный текст)
		- комментарий
		- ТипАннотации
		- Разметчик
	- "тип аннотации"
	  - человекочитаемое название
		- ключ (ключи являются materialized path и позволяют делать из типов аннотаций иерархичную структуру)
  - "пользователь"
	  - ФИО
		- is_staff
- [ ] (1) добавить модели в админку
- [ ] (3) добавить сериалайзеры и представления для моделек
- [X] (1) добавить общее приложение
- [ ] (1) Добавить модельки:
	- "пользователь"
	  - 
	- "токен"
	  - Пользователь
		- value
- [ ] (1) добавить сериалайзеры и представления для моделек
- [ ] (3) сгенерировать клиент (в этот момент можно начинать фронт)
- [ ] (1) Добавить модельку "загруженный файл"
- [ ] (2) Добавить ручку для заливки файлов
- [ ] (4) Добавить простой поиск по корпусу
- [ ] (?) Добавить систему доступов
  - ??? какие нужны доступы

Итого: 21

- [ ] найти модельку для автоматической проверки (наташа?) 

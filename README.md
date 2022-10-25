1. в корне
   docker-compose up --build redis

2. в backend
   uvicorn main:app --reload

3. http://127.0.0.1:8000/docs#/

1) создаем голосования http://127.0.0.1:8000/docs#/default/update_item_votes__post

2) создаем ответы http://127.0.0.1:8000/docs#/default/create_answer_answer__post

3) выбираем голосование http://127.0.0.1:8000/docs#/default/get_all_votes_votes__get

4) проверяем выборку по голосованию http://127.0.0.1:8000/docs#/default/get_answers_count_answers_count__vote_id___get

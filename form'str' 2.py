# Переменные
team1_num= 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
tima_avg = 45.2
challenge_result = 'Победа команды Волшебников даннных'

# Изпользывание %
print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодняв командах участников: %d И %d !' % (team1_num, team2_num))

# Изпользывание format()
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {:.2f} C !'.format(team2_time))

# Изпользывание f-строка
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {tima_avg:.2f} секунды на задачу!')
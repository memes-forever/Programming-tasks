--SQL Task 1
--Дана таблица отсортированная по id.
--При этом несмотря на то, что значения поля id последовательны, часть значений пропущено.
--Требуется написать запрос, который выведет диапазоны id, в которых нет пропусков.
--
--Таблица                  Пример ответа
--+------+------+          +----------+--------+
--|  id  | data |          | start_id | end_id |
--+------+------+          +----------+--------+
--| 2    |  ... |          |        2 | 3      |
--| 3    |  ... |          |       11 | 13     |
--| 11   |  ... |          |       27 | 27     |
--| 12   |  ... |          |       33 | 35     |
--| 13   |  ... |          |       42 | ...    |
--| 27   |  ... |          |      ... | ...    |
--| 33   |  ... |          |      ... | N      |
--| 34   |  ... |          +----------+--------+
--| 35   |  ... |
--| 42   |  ... |
--| ...  |  ... |
--| N    |  ... |
--+------+------+


with test_data as (
	-- Генерим тестовые данные
	select id
	from (select generate_series as id from generate_series(2,43)) as d
	where id not in (4,5,6,7,8,9,10,14,15,16,17,22,23,24,25,27,28,36,37,38,39,40,41)
	order by id
),
test_data_with_window AS (
	SELECT
		id,
		lag(id, 1, id-1) OVER (ORDER BY id) AS id_lag, -- Вычисляем предыдущую строку
		lead(id, 1, id+1) OVER (ORDER BY id) AS id_lead, -- Вычисляем следующую строку
		case
			when id -1 = lag(id, 1, id-1) OVER (ORDER BY id) then 0
			else 1
	  end as g_lag -- проставляем первому попавшемосу диапазону еденицу
	FROM test_data
),
main as (
	select
	  test_data_with_window.*,
	  sum(g_lag) over (order by id) as g_sum -- сумируем единицы по группам, тем саммым получаем уникальные группы диапазонов
	from test_data_with_window
)
select
	'Без пропуска:' as t,
 	min(id) as min_id,
 	max(id) as max_id
from main
group by 1, g_sum -- группировка по группе
union all -- соединяем 2 ответа
select
	'С пропуском:' as t,
	id+1 as min_id,
    id_lead-1 as max_id
FROM main
WHERE id_lead - 1 >= id + 1 -- следующая строка -1 больше или равна текущей +1
-- сортируем результат
order by min_id

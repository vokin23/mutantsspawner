# Mutants Spawner Editor
Данная программа редактирует файлы мода Mutants Spawner

Описание: 
1. day.txt - файл самого мода, в котором находятся строки для спауна.
2. evening.txt - файл самого мода, в котором находятся строки для спауна.
3. morning.txt - файл самого мода, в котором находятся строки для спауна.
4. night.txt - файл самого мода, в котором находятся строки для спауна.
5. all_mutant.txt - файл, в который мы вносим координаты ,взятые из игры DayZ, и classname самого животного через пробел. Форму файлы соблюдать обязательно.
6. mutants_editor_console.py - прогамма, которой на входе требуется: координата ( Пример: Position: <2803.124124, 2131241, 4220.950195>), количество мутантов, которые будут спаунятся на этой коорденате (любое целое число больше 0) и classname самого мутанта.
7. mutants_editor_file.py - анлог 6 пункта, только предназначен для массового добавления мутантов. Данные берет из all_mutant.txt и переносит по всем файлам в нужной форме.
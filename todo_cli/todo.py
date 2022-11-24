import click

@click.group()
@click.pass_context
def todo(ctx):
    ctx.ensure_object(dict)
    """ Откройте файл todo.txt - первая строка содержит последний ID, остальные - задачи и ID """
    with open('./todo.txt') as f:
        content = f.readlines()

    ctx.obj['LATEST'] = int(content[:1][0])
    ctx.obj['TASKS'] = {en.split('````')[0]:en.split('````')[1][:-1] for en in content[1:]}

@todo.command()
@click.pass_context
def tasks(ctx):
    """ Показать задачи """
    if ctx.obj['TASKS']:
        click.echo('Ваши задачи\n**********')
        #Итерация по всем задачам, хранящимся в контексте
        for i, task in ctx.obj['TASKS'].items():
            click.echo('. ' + task + ' (ID: ' + i + ')')
        click.echo('')
    else:
        click.echo('Пока нет задач! Используйте ADD, чтобы добавить первую.\n')

@todo.command()
@click.pass_context
@click.option('-add', '--add_task', prompt='Введите задачу для добавления')
def add(ctx, add_task):
    """ Добавить задачу """
    if add_task:
        #Добавить задачу в список в контексте
        ctx.obj['TASKS'][ctx.obj['LATEST']] = add_task
        click.echo('Добавлена задача "' + add_task + '" с ID ' + str(ctx.obj['LATEST']))
        #Открыть todo.txt и записать текущий индекс и задачи с идентификаторами (разделенные " ```")
        curr_ind = [str(ctx.obj['LATEST'] + 1)]
        tasks = [str(i) + '````' + t for (i, t) in ctx.obj['TASKS'].items()]
        with open('./todo.txt', 'w') as f:
            f.writelines(['%s\n' % en for en in curr_ind + tasks])

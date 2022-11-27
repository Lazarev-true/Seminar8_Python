def progress():
    from progress.bar import IncrementalBar
    import time

    bar = IncrementalBar('Загрузка таблицы')
    for i in range(100):
 
        time.sleep(0.03)
        bar.next()
    bar.finish()

# Simulator of Social Inequality

Общество можно представить как пирамиду, на вершине которой находится его элита, 
состоящая из людей, обладающих властью и большими материальными ценностями, а 
нижние этажи отведены, как принято говорить, простым людям

# Для работы проекта..
```
    pip install matplotlib, customtkinter
```

# Описание
Зависть многочисленных жителей нижних этажей к богатству тех немногих, кто 
оказался на самом верху, часто бывает трудно отличить от любви к справедливости.
Так как элита общества расставаться со своими богатствами не собирается, то 
законное стремление простых людей жить лучше всегда наталкивается на 
сопротивление жителей верхних этажей этой пирамиды. Таким образом, пирамида
нашего общества вечный повод для револю ционной борьбы бедных с богатыми, а
история человечества история борьбы за социальное равенство. Социологи, многим
из которых чувство зависти тоже не было чуждо, не раз давали советы, как построить
общество, где все были бы равны. Если искать геометрические аналогии, то «общество
равных» можно было бы представить себе в виде диска очень большого диаметра с 
высокой башней в центре, из окон которой выглядывают несколько представителей 
из «равных», ответственных за поддержание равенства.
К сожалению, история показала, что теория построения «общества равных» не 
выдерживает испытание практикой хотя бы из-за того, что некоторые люди не 
хотят быть равными другим и таким своим поведением отвлекают непомерно большие 
материальные средства общества на поддержание равенства. Не вдаваясь в 
дальнейшую полемику о том, каким должно быть современное общество, чтобы 
каждому в нем жилось хорошо, попытаемся лишь ответить на вопрос, почему торговые 
отношения между членами общества приводят к тому, что в руках меньшей части 
общества оказывается большая часть его богатств. Но сначала посмотрим, 
какие существуют оценки социального неравенства.

# Правила торговли
1. раз в день каждого гражданина оповещают о том, с кем ему сегодня встречаться 
для торговли, этот список генерируется компьютером и является случайным;
2. когда происходит запланированная встреча продавца и покупателя, компьютер 
случайным образом определяет того, кто получает выгоду от торговли, и ее размер; 
соответственно, богатство неудачника уменьшается на ту же величину;
3. выгода от торговли может быть:
    * постоянной величиной, как например, в некоторых видах лотереи или 
    случайных сбоях компьютера кассового аппарата,
    * случайно определяемой долей богатства неудачника,
    * случайно определяемой долей суммарного богатства участников сделки;
4. в тех случаях когда государство собирает налог со всех, кто получил выгоду во 
время торговли, оно распределяет его поровну среди всех членов общества.
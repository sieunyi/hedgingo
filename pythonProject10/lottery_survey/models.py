from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range
)


class Player(BasePlayer):
    # Consent form fields
    consent_age = models.BooleanField(label="Tengo 18 años o más.")
    consent_read = models.BooleanField(label="He leído y entiendo la información anterior.")
    consent_participate = models.BooleanField(label="Quiero participar en esta investigación y continuar con el estudio.")

    # Survey fields
    age_check = models.BooleanField(label="¿Tiene 18 años de edad o más?", choices=[[True, 'Sí'], [False, 'No']])
    gender = models.StringField(label="¿Con qué género te identificas?", choices=['Femenino', 'No binario', 'Masculino'], widget=widgets.RadioSelect)
    career = models.StringField(label="¿Cuál es tu carrera?")
    native_language = models.StringField(label="¿Cuál es tu lengua materna?")
    university_year = models.StringField(label="¿En qué año de la universidad estás?", choices=['Primer año', 'Segundo año', 'Tercer año', 'Cuarto año', 'Posgrado', 'Otro'], widget=widgets.RadioSelect)
    gpa = models.FloatField(label="¿Cuál es tu promedio actual? (0-5, hasta 4 decimales)", min=0, max=5)
    smoker = models.BooleanField(label="¿Eres fumador?", choices=[[True, 'Sí'], [False, 'No']], widget=widgets.RadioSelect)
    alcohol = models.BooleanField(label="¿Practicas el consumo excesivo de alcohol?", choices=[[True, 'Sí'], [False, 'No']], widget=widgets.RadioSelect)
    drugs = models.BooleanField(label="¿Consumes drogas recreativas?", choices=[[True, 'Sí'], [False, 'No']], widget=widgets.RadioSelect)
    weekly_spending = models.CurrencyField(label="¿Cuál es tu gasto semanal en pesos mexicanos?")

    # Cognitive Reflection Test
    crt_linda = models.StringField(label="¿Cuál de las siguientes dos alternativas es más probable?", choices=['Linda es cajera de banco.', 'Linda es cajera de banco y activista en el movimiento feminista.'], widget=widgets.RadioSelect)
    crt_bat = models.FloatField(label="¿Cuántos dólares cuesta la pelota?")
    crt_widget = models.IntegerField(label="¿Cuántos minutos tardarían 100 máquinas en hacer 100 widgets?")
    crt_lake = models.IntegerField(label="¿Cuántos días tardaría en cubrir la mitad del lago?")
    crt_double = models.StringField(label="En 2021, ¿cuánto podrás comprar con tu ingreso?:", choices=['Más que hoy.', 'Exactamente lo mismo que hoy.', 'Menos que hoy.'], widget=widgets.RadioSelect)

    # Financial Literacy
    fin_change = models.CurrencyField(label="¿Cuánto cambio deberías recibir en pesos mexicanos?")
    fin_lottery = models.CurrencyField(label="¿Cuánto recibirá cada uno en pesos mexicanos?")
    fin_sale = models.CurrencyField(label="¿Cuánto costará en la venta en pesos mexicanos?")
    fin_cardealer = models.CurrencyField(label="¿Cuánto costó el coche nuevo en pesos mexicanos?")
    fin_interest = models.CurrencyField(label="¿Cuánto tendrás en la cuenta en pesos mexicanos al final de dos años?")
    fin_disease = models.IntegerField(label="¿Cuántas personas de 1,000 se esperaría que contrajeran la enfermedad?")

    # Risk Attitudes
    risk_general = models.IntegerField(label="¿Cómo calificarías tu disposición a asumir riesgos en general?", min=1, max=10)
    risk_driving = models.IntegerField(label="¿Cómo calificarías tu disposición a asumir riesgos al conducir?", min=1, max=10)
    risk_career = models.IntegerField(label="¿Cómo calificarías tu disposición a asumir riesgos en tu carrera profesional?", min=1, max=10)
    risk_health = models.IntegerField(label="¿Cómo calificarías tu disposición a asumir riesgos con respecto a tu salud?", min=1, max=10)

    # Decision Making Scenarios
    scenario_jar = models.StringField(label="¿Qué frasco prefieres para adivinar el color de una bola?", choices=['Prefiero adivinar el color de una bola del frasco 1.', 'Soy indiferente.', 'Prefiero adivinar el color de una bola del frasco 2.'], widget=widgets.RadioSelect)
    monty_hall = models.StringField(label="¿Te conviene cambiar tu elección?", choices=['Prefiero mantener mi elección original (Puerta número 1).', 'No importa si cambio o no.', 'Prefiero cambiar a la Puerta número 2.'], widget=widgets.RadioSelect)

    # Timing fields
    decision_time = models.FloatField()
    continue_field = models.StringField(label="")
    exit_survey_completed = models.BooleanField(initial=False)

    # Fields from the second Player class
    alpha = models.FloatField(min=0, max=1)
    p = models.FloatField()
    one_minus_p = models.FloatField()
    x1_l = models.FloatField()
    x1_h = models.FloatField()
    x2_h = models.FloatField()
    x2_l = models.FloatField()





class Constants(BaseConstants):
    name_in_url = 'hedging'
    players_per_group = None
    num_rounds = 45
    individual_rounds = 45

    scenarios = [
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [0.4, 0.7, 1.1, 1.5, 2.0, 2.6, 3.3, 4.3, 6.3],
            'x2_l_values': [-6.3, -4.3, -3.3, -2.6, -2.0, -1.5, -1.1, -0.7, -0.4]
        },
        {
            'p_values': [0.5] * 9,
            'one_minus_p_values': [0.5] * 9,
            'x1_l_values': [-8, -7, -6, -5, -4, -3, -2, -1, 0],
            'x1_h_values': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'x2_h_values': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'x2_l_values': [-8, -7, -6, -5, -4, -3, -2, -1, 0]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [6.4, 4.0, 3.1, 2.4, 2.0, 1.6, 1.3, 1.0, 0.7],
            'x2_l_values': [-0.7, -1.0, -1.3, -1.6, -2.0, -2.4, -3.1, -4.0, -6.0]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [0.4] * 9,
            'x2_l_values': [-6.3, -4.6, -4.0, -3.7, -3.6, -3.7, -4.0, -4.6, -6.3]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [6.3, 4.6, 4.0, 3.7, 3.6, 3.7, 4.0, 4.6, 6.3],
            'x2_l_values': [-0.4] * 9
        }
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            scenario_index = (player.round_number - 1) // 9
            round_in_scenario = (player.round_number - 1) % 9
            scenario = Constants.scenarios[scenario_index]

            player.p = scenario['p_values'][round_in_scenario]
            player.one_minus_p = scenario['one_minus_p_values'][round_in_scenario]
            player.x1_l = scenario['x1_l_values'][round_in_scenario]
            player.x1_h = scenario['x1_h_values'][round_in_scenario]
            player.x2_h = scenario['x2_h_values'][round_in_scenario]
            player.x2_l = scenario['x2_l_values'][round_in_scenario]


class Group(BaseGroup):
    pass


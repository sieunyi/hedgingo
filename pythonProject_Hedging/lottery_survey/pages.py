from otree.api import Page
from .models import Constants, Player, Subsession
import random

class Roulette(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # Randomly select one of the 45 rounds
        selected_round = random.randint(1, Constants.num_rounds)
        player_in_selected_round = self.player.in_round(selected_round)

        # Get the scenario and round information for the selected round
        scenario_index = (selected_round - 1) // 9
        round_in_scenario = (selected_round - 1) % 9
        scenario = Constants.scenarios[scenario_index]

        # Safely get the alpha value, use a default if it's None
        alpha = player_in_selected_round.field_maybe_none('alpha')
        if alpha is None:
            alpha = 1  # Default value if alpha is not set

        p = round(scenario['p_values'][round_in_scenario], 2)
        one_minus_p = round(1 - p, 2)  # Fixed: use p instead of player.p
        x1_l = scenario['x1_l_values'][round_in_scenario]
        x1_h = scenario['x1_h_values'][round_in_scenario]
        x2_l = scenario['x2_l_values'][round_in_scenario]
        x2_h = scenario['x2_h_values'][round_in_scenario]

        expected_value = (p * (alpha * x1_l + (1 - alpha) * x2_h) + one_minus_p * (alpha * x1_h + (1 - alpha) * x2_l))

        return {
            'selected_round': selected_round,
            'alpha': round(alpha, 2),
            'p': p,
            'one_minus_p': one_minus_p,
            'x1_l': round(x1_l, 1),
            'x1_h': round(x1_h, 1),
            'x2_l': round(x2_l, 1),
            'x2_h': round(x2_h, 1),
            'expected_value': round(expected_value, 2),
            'Constants': Constants
        }
class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent_age', 'consent_read', 'consent_participate']
    def is_displayed(self):
        return self.round_number == 1


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class LotterySurvey(Page):
    form_model = 'player'
    form_fields = ['alpha']

    def vars_for_template(self):
        # Ensure shuffled_rounds exists
        if 'shuffled_rounds' not in self.session.vars:
            self.session.vars['shuffled_rounds'] = Subsession.generate_shuffled_rounds()

        shuffled_round = self.session.vars['shuffled_rounds'][self.round_number - 1]

        # Store the original round number and scenario in player's model
        self.player.original_round_number = shuffled_round

        scenario_index = (shuffled_round - 1) // 9
        round_in_scenario = (shuffled_round - 1) % 9
        scenario = Constants.scenarios[scenario_index]

        # Save original scenario number
        self.player.original_scenario_number = scenario_index + 1

        # Calculate p and one_minus_p with rounding to avoid floating-point precision issues
        p = round(scenario['p_values'][round_in_scenario], 2)
        one_minus_p = round(1 - p, 2)

        vars_dict = {
            'round_number': self.round_number,
            'original_round_number': shuffled_round,
            'num_rounds': Constants.num_rounds,
            'scenario_number': scenario_index + 1,
            'round_in_scenario': round_in_scenario + 1,
            'p': p,
            'one_minus_p': one_minus_p,
            'x1_l': round(scenario['x1_l_values'][round_in_scenario], 2),
            'x1_h': round(scenario['x1_h_values'][round_in_scenario], 2),
            'x2_l': round(scenario['x2_l_values'][round_in_scenario], 2),
            'x2_h': round(scenario['x2_h_values'][round_in_scenario], 2),
        }
        return vars_dict


class PracticeRound(Page):
    form_model = 'player'
    form_fields = ['alpha']

    def is_displayed(self):
        return self.round_number <= Constants.practice_rounds

    def vars_for_template(self):
        scenario = Constants.practice_scenarios[0]
        round_in_scenario = self.round_number

        # Store the practice round number and scenario
        self.player.original_round_number = self.round_number
        self.player.original_scenario_number = 1

        # Use the specific values for each round
        p = round(scenario['p_values'][round_in_scenario - 1], 2)
        one_minus_p = round(scenario['one_minus_p_values'][round_in_scenario - 1], 2)

        vars_dict = {
            'round_number': self.round_number,
            'num_rounds': Constants.practice_rounds,
            'scenario_number': 1,
            'round_in_scenario': round_in_scenario,
            'p': p,
            'one_minus_p': one_minus_p,
            'x1_l': round(scenario['x1_l_values'][round_in_scenario - 1], 2),
            'x1_h': round(scenario['x1_h_values'][round_in_scenario - 1], 2),
            'x2_l': round(scenario['x2_l_values'][round_in_scenario - 1], 2),
            'x2_h': round(scenario['x2_h_values'][round_in_scenario - 1], 2),
        }
        return vars_dict


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent_age', 'consent_read', 'consent_participate']

    def is_displayed(self):
        return self.round_number == 1
    def error_message(self, values):
        if not (values['consent_age'] and values['consent_read'] and values['consent_participate']):
            return 'Debe aceptar todos los elementos de consentimiento para continuar.'

class example(Page):
    def is_displayed(self):
        return self.round_number == 1

class example2(Page):
    def is_displayed(self):
        return self.round_number == 1


class example3(Page):
    def is_displayed(self):
        return self.round_number == 1

class earning(Page):
    def is_displayed(self):
        return self.round_number == 1

class example4(Page):
    def is_displayed(self):
        return self.round_number == 1

class welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Introduction2(Page):
    def is_displayed(self):
        return self.round_number == 1


class SurveyIntroduc(Page):
    template_name = 'lottery_survey/SurveyIntroduc.html'

    def is_displayed(self):
        return self.round_number == Constants.individual_rounds + 4


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age_check', 'gender', 'career', 'native_language', 'university_year', 'gpa', 'smoker', 'alcohol', 'drugs', 'weekly_spending']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_linda', 'crt_bat', 'crt_widget', 'crt_lake', 'crt_double']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class FinancialLiteracy(Page):
    form_model = 'player'
    form_fields = ['fin_change', 'fin_lottery', 'fin_sale', 'fin_disease', 'fin_cardealer', 'fin_interest']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class RiskAttitudes(Page):
    form_model = 'player'
    form_fields = ['risk_general', 'risk_driving', 'risk_career', 'risk_health']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class DecisionMakingScenarios(Page):
    form_model = 'player'
    form_fields = ['scenario_jar', 'monty_hall']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class MatrixReasoning(Page):
    form_model = 'player'
    form_fields = ['Matrix_B06', 'Matrix_B09', 'Matrix_B11', 'Matrix_C02', 'Matrix_C05',
                   'Matrix_C12', 'Matrix_D05', 'Matrix_D07', 'Matrix_E07']
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class EndPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.exit_survey_completed = True
    pass


class ComprehensionCheck(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2', 'question_3']

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        errors = {}
        if values['question_1'] != '20%':
            errors['question_1'] = 'This answer is incorrect'
        if values['question_2'] != 'When L1 increases, L2 decreases (Inverse Relationship)':
            errors['question_2'] = 'This answer is incorrect'
        if values['question_3'] != '50% * 10 + 50% * (-10) = 0':
            errors['question_3'] = 'This answer is incorrect'
        if errors:
            return errors
        else:
            # If no errors, set passed_comprehension to True
            self.player.passed_comprehension = True
            return None

    def vars_for_template(self):
        return {
            'show_success': self.player.passed_comprehension if hasattr(self.player, 'passed_comprehension') else False
        }



class EarningsExplanation(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1  # Only show on the first round



# Define the initial sequence
initial_sequence = [
    welcome,
    Introduction,
    Introduction2,
    earning,
    example2,
  #  example,
    example3,

]

practice_rounds = [PracticeRound]

# Define the main experiment sequence
main_sequence = [
    ComprehensionCheck,
    EarningsExplanation,
    LotterySurvey,
    Roulette,
    SurveyIntroduc,
    Demographics,
    CognitiveReflectionTest,
    FinancialLiteracy,
    RiskAttitudes,
    DecisionMakingScenarios,
    EndPage
]

# Combine all sequences
page_sequence = initial_sequence + practice_rounds + main_sequence
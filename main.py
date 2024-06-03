import json, difflib
import datetime as dt

class Main:


    # sets current date with specific format
    current_date = dt.datetime.now().strftime('%B, %Y')
    # json data
    with open('data.json') as json_file:
        data = json.load(json_file)


    def find_relevant_skills(self) -> list:
        '''
        Finds all of your skills used within the job posting wihtin `full_posting.txt`.
        '''
        your_skills = self.data['full_skills_list']
        # gets full posting data
        character_remove_list = [':', ',']
        with open("full_posting.txt", "r") as posting:
            full_posting_words = []
            for line in posting:
                for word in line.split():
                    for char in character_remove_list:
                        word = word.replace(char, '')
                    full_posting_words.append(word)
        # find relevant skills
        relevant_skills = []
        for posting_word in full_posting_words:
            max_similarity = .8
            for skill in your_skills:
                similarity = difflib.SequenceMatcher(None, posting_word, skill).ratio()
                if similarity > max_similarity:
                    if posting_word not in relevant_skills:
                        relevant_skills.append(posting_word)
        print(relevant_skills)
        return relevant_skills

    @staticmethod
    def to_comma_string(list):
        output = ''
        length = len(list)
        for count, item in enumerate(list):
            if count+1 == length:
                output += f'and {item}'
            else:
                output += f'{item}, '
        return output

    def write_to_file(self):
        '''
        Writes text to a file.
        '''
        # you
        your_name = self.data['you']['name']
        phone_number = self.data['you']['phone_number']
        email = self.data['you']['email']
        your_address_1 = self.data['you']['address_1']
        your_address_2 = self.data['you']['address_2']
        github = self.data['you']['github']
        linked_in = self.data['you']['linked_in']
        adjectives = self.data['you']['adjectives']
        reason_for_coding = self.data['you']['reason_for_coding']
        hook = self.data['you']['hook']
        prior_job = self.data['you']['prior_job']
        former_industry = self.data['you']['former_industry']
        skills = self.to_comma_string(self.data['you']['skills'])
        positive_qualities = self.data['you']['positive_qualities']
        stack_focus = self.data['you']['stack_focus']
        # relevant_project
        project_name = self.data['relevant_project']['name']
        project_description = self.data['relevant_project']['description']
        project_technologies = self.data['relevant_project']['technologies']
        # company
        company_name = self.data['company']['name']
        company_address_1 = self.data['company']['address_1']
        company_address_2 = self.data['company']['address_2']
        job_title = self.data['company']['job_title']
        stack_focus = self.data['company']['stack_focus']
        hiring_manager_name = self.data['company']['hiring_manager_name']
        mission = self.data['company']['mission']

        para_sentences = [
            f'{hook} I am a {adjectives} former {prior_job} who has recently transitioned into Software Engineering and am now excited to be applying for this position.',
            # f'My {former_industry} experience gave me numerous transferable skills such as {skills}, but I have since put in the work to gain essential tech skills making me an excellent candidate for this position.',
            f'My love for {reason_for_coding} led me to programming, and I decided to further my education by attending App Academy\'s 16-week, 1000+ hour Software Engineering program where I honed my expertise in Python, React, Redux, JavaScript, HTML, CSS, PostgreSQL, along with many other technologies.',
            f'In my time at App Academy, I built several projects including {project_name}, a {project_description} using {project_technologies} along with several others you can view on my resume and portfolio site as linked above.',
            f'Given my project experience, I am confident in my ability to contribute from day one as a {stack_focus} Developer as I\'ve built both alone and within a group using an Agile workflow with incredibly quick turnaround times.',
            'As evidenced by my career trajectory, I am able to learn new skills and technologies quickly and to completion.',
            f'Combining my {positive_qualities} along with my recently acquired technical skills, I know I would be a perfect fit for {company_name}.',
            f'I have seen the work you do and am confident I can contribute to the team as a {job_title} and help you achieve {mission}.',
            f'I\'m excited about this role and looking forward to hearing from you soon.'
        ]

        header = f'{your_name}\n{your_address_1} - {your_address_2} - {phone_number} - {email}\n{linked_in}\n{github}'
        company_info = f'\n\n{self.current_date}\n\n{company_name}\n{company_address_1}\n{company_address_2}'
        intro = f'\n\nDear {hiring_manager_name},\n\n{" ".join(para_sentences)}'
        goodbye = f'\n\nSincerely,\n{your_name}'

        combined = header + company_info + intro + goodbye
    
        with open(f'starter_cover_letter.txt', "w") as outfile:
            outfile.write(combined)


if __name__ == '__main__':
    app = Main()
    # app.find_relevant_skills()
    app.write_to_file()

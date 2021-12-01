import json
import datetime as dt

class main:
    
    current_date = dt.datetime.now().strftime('%d %B %Y')

    with open('data.json') as json_file:
        data = json.load(json_file)


    def write_to_file(self):
        # you
        your_name = self.data['you']['name']
        phone_number = self.data['you']['phone_number']
        email = self.data['you']['prior_job']
        address = self.data['you']['prior_job']
        github = self.data['you']['github']
        linked_in = self.data['you']['linked_in']
        adjectives = self.data['you']['prior_job']
        skills = ', '.join(self.data['you']['skills'])
        reason_for_coding = self.data['you']['prior_job']
        hook = self.data['you']['prior_job']
        prior_job = self.data['you']['prior_job']
        former_industry = self.data['you']['former_industry']
        positive_qualities = self.data['you']['prior_job']
        stack_focus = self.data['you']['prior_job']
        prior_job = self.data['you']['prior_job']
        prior_job = self.data['you']['prior_job']
        prior_job = self.data['you']['prior_job']
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
            f'My {former_industry} experience gave me numerous transferable skills such as {skills}, but I have since put in the work to gain essential tech skills making me an excellent candidate for this position.',
            f'My love for {reason_for_coding} led me to programming, and I decided to further my education by attending App Academy\'s 16-week, 1000+ hour Software Engineering program where I honed my expertise in Python, React, Redux, JavaScript, HTML, CSS, PostgreSQL, along with many other technologies.',
            f'In my time at App Academy, I built several projects including {project_name}, a {project_description} using {project_technologies} along with several others you can view on my resume and portfolio site as linked above.',
            f'Given my project experience, I am confident in my ability to contribute from day one as a {stack_focus} Developer as I\'ve built both alone and within a group using an Agile workflow with incredibly quick turnaround times.',
            'As evidenced by my career trajectory, I am able to learn new skills and technologies quickly and to completion.',
            f'Combining my {positive_qualities} along with my recently acquired technical skills, I know I would be a perfect fit for {company_name}.',
            f'I have seen the work you do and am confident I can contribute to the team as a {job_title} and help you achieve {mission}.',
            f'I\'m excited about this role and looking forward to hearing from you soon.'
        ]

        text = f'''
        {your_name}
        {address} - {phone_number} - {email}
        {linked_in}
        {github}

        {self.current_date}

        {company_name}
        {company_address_1}
        {company_address_2}

        Dear {hiring_manager_name},

        {' '.join(para_sentences)}

        Sincerely, 
        {your_name}
        '''
    
        with open(f'starter_cover_letter.txt', "w") as outfile:
            outfile.write(text)



main().write_to_file()

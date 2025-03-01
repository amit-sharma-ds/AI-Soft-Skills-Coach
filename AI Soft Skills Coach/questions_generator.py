def generate_dynamic_question_and_answer(domain, experience_level):

    experienced_questions = {
        "general":[
            {
                "question": "Can you describe your professional background?",
                "ideal_answer": "I have over 5 years of experience in software development, specializing in web applications. I have worked with various technologies and led multiple successful projects."
            },
            {
                "question": "What motivates you in your work?",
                "ideal_answer": "I am motivated by challenges and the opportunity to solve complex problems. I also find fulfillment in mentoring junior team members and contributing to their growth."
            },
            {
                "question": "Why are you leaving your current job?",
                "ideal_answer": "I am looking for new challenges and opportunities for growth. I believe that this position aligns well with my career goals and aspirations."
            },
            {
                "question": "How do you handle failure?",
                "ideal_answer": "I view failure as a learning opportunity. I analyze what went wrong, seek feedback, and apply those lessons to future projects."
            },
            {
                "question": "What are your long-term career goals?",
                "ideal_answer": "My long-term career goal is to take on a leadership role where I can influence project direction and mentor others in the field."
            },
            {
                "question": "How do you stay current with industry trends?",
                "ideal_answer": "I stay current by attending industry conferences, participating in online courses, and following thought leaders on social media."
            },
            {
                "question": "What is your approach to work-life balance?",
                "ideal_answer": "I prioritize work-life balance by setting boundaries, managing my time effectively, and ensuring I make time for personal interests and family."
            },
            {
                "question": "How do you handle tight deadlines?",
                "ideal_answer": "I handle tight deadlines by prioritizing tasks, communicating with my team, and focusing on delivering high-quality work efficiently."
            },
            {
                "question": "What do you consider your biggest professional achievement?",
                "ideal_answer": "My biggest achievement was leading a project that improved system performance by 30%, resulting in significant cost savings for the company."
            },
            {
                "question": "How do you approach decision-making?",
                "ideal_answer": "I approach decision-making by gathering relevant data, consulting with team members, and considering the potential impact of each option before making a choice."
            }

        ],
        "managerial": [
            {
                "question": "How do you manage team dynamics?",
                "ideal_answer": "I manage team dynamics by fostering open communication, encouraging collaboration, and addressing conflicts promptly to maintain a positive work environment."
            },
            {
                "question": "What is your approach to project management?",
                "ideal_answer": "My approach to project management involves setting clear goals, defining roles and responsibilities, and using project management tools to track progress and ensure accountability."
            },
            {
                "question": "How do you handle underperforming team members?",
                "ideal_answer": "I address underperformance by having one-on-one discussions to understand the challenges they face and providing support or resources to help them improve."
            },
            {
                "question": "What strategies do you use for effective delegation?",
                "ideal_answer": "I delegate tasks based on team members' strengths and interests, ensuring they have the resources and support needed to succeed."
            },
            {
                "question": "How do you measure team success?",
                "ideal_answer": "I measure team success through key performance indicators (KPIs), project outcomes, and team feedback to assess both productivity and morale."
            },
            {
                "question": "How do you approach change management?",
                "ideal_answer": "I approach change management by communicating the reasons for change, involving the team in the process, and providing training and support to ease the transition."
            },
            {
                "question": "What is your experience with budget management?",
                "ideal_answer": "I have experience managing project budgets by tracking expenses, forecasting costs, and ensuring that we stay within budget while delivering quality results."
            },
            {
                "question": "How do you ensure alignment with company goals?",
                "ideal_answer": "I ensure alignment with company goals by regularly communicating objectives to the team, setting measurable targets, and reviewing progress in team meetings."
            },
            {
                "question": "How do you handle feedback from upper management?",
                "ideal_answer": "I handle feedback from upper management by actively listening, seeking clarification if needed, and implementing changes to improve our processes and outcomes."
            },
            {
                "question": "What is your approach to mentoring junior team members?",
                "ideal_answer": "I approach mentoring by providing guidance, sharing my experiences, and encouraging them to take on challenging tasks to foster their growth."
            }
 
        ],

        "technical": [
            {
                "question": "What technologies are you currently working with?",
                "ideal_answer": "I am currently working with React for front-end development, Node.js for back-end services, and MongoDB for database management."
            },
            {
                "question": "Can you explain a complex technical concept to a non-technical person?",
                "ideal_answer": "Sure! I can explain how a REST API works by comparing it to a restaurant menu, where the menu lists available dishes, and you can order what you want through the waiter, who communicates with the kitchen."
            },
            {
                "question": "What is your experience with cloud computing?",
                "ideal_answer": "I have experience deploying applications on AWS and Azure, utilizing services like EC2, S3, and Azure Functions to build scalable solutions."
            },
            {
                "question": "How do you ensure code quality?",
                "ideal_answer": "I ensure code quality by following coding standards, conducting code reviews, and writing unit tests to validate functionality."
            },
            {
                "question": "What is your experience with Agile methodologies?",
                "ideal_answer": "I have worked in Agile environments for several years, participating in daily stand-ups, sprint planning, and retrospectives to continuously improve our processes."
            },
            {
                "question": "Can you describe a challenging technical problem you solved?",
                "ideal_answer": "I once faced a performance issue in a web application. After profiling the code, I identified bottlenecks and optimized database queries, resulting in a 50% reduction in load time."
            },
            {
                "question": "What tools do you use for version control?",
                "ideal_answer": "I primarily use Git for version control, along with platforms like GitHub and GitLab for collaboration and code review."
            },
            {
                "question": "How do you approach learning new technologies?",
                "ideal_answer": "I approach learning new technologies by starting with online tutorials, building small projects, and gradually integrating them into my work."
            },
            {
                "question": "What is your experience with data analysis?",
                "ideal_answer": "I have experience using Python libraries like Pandas and NumPy for data analysis, as well as visualization tools like Matplotlib and Tableau."
            },
            {
                "question": "How do you handle technical debt?",
                "ideal_answer": "I handle technical debt by regularly reviewing our codebase, prioritizing refactoring tasks, and ensuring that we allocate time in our sprints to address it."
            }

        ]

    }

    fresher_questions = {
        "general": [
            {
                "question": "Can you introduce yourself?",
                "ideal_answer": "I am a recent graduate with a degree in Computer Science. I am passionate about problem-solving and have worked on projects involving data analysis and web development during my academic career."
            },
            {
                "question": "What are your strengths?",
                "ideal_answer": "I am a quick learner and have strong analytical skills. I am also a team player and enjoy collaborating with others to achieve common goals."
            },
            {
                "question": "Why do you want to work here?",
                "ideal_answer": "I admire your company's commitment to innovation and quality. I believe that working here will provide me with valuable experience and opportunities to grow."
            },
            {
                "question": "What are your hobbies?",
                "ideal_answer": "I enjoy coding in my free time, participating in hackathons, and reading about new technologies. I also like to play chess to improve my strategic thinking."
            },
            {
                "question": "How do you prioritize your tasks?",
                "ideal_answer": "I prioritize tasks based on deadlines and importance. I use tools like to-do lists and project management software to stay organized."
            },
            {
                "question": "What is your greatest achievement?",
                "ideal_answer": "My greatest achievement was leading a team project in college where we developed a web application that won the best project award at our university's tech fest."
            },
            {
                "question": "How do you handle stress?",
                "ideal_answer": "I handle stress by staying organized and breaking tasks into smaller, manageable parts. I also practice mindfulness techniques to stay calm."
            },
            {
                "question": "Where do you see yourself in five years?",
                "ideal_answer": "In five years, I see myself as a skilled software developer, contributing to impactful projects and possibly taking on leadership responsibilities."
            },
            {
                "question": "What do you know about our company?",
                "ideal_answer": "I know that your company is a leader in the tech industry, known for its innovative solutions and commitment to customer satisfaction."
            },
            {
                "question": "How do you stay updated with industry trends?",
                "ideal_answer": "I stay updated by following tech blogs, participating in online courses, and attending webinars and workshops related to my field."
            }
        ],
        "managerial": [
            {
                "question": "How do you handle group projects?",
                "ideal_answer": "I believe in open communication and assigning roles based on individual strengths. During my final year project, I coordinated tasks and ensured timely completion, resulting in a successful presentation."
            },
            {
                "question": "How do you resolve conflicts within a team?",
                "ideal_answer": "I address conflicts by facilitating open discussions, encouraging team members to express their viewpoints, and working towards a mutually agreeable solution."
            },
            {
                "question": "What is your leadership style?",
                "ideal_answer": "My leadership style is collaborative. I believe in empowering team members, encouraging their input, and fostering a supportive environment."
            },
            {
                "question": "How do you motivate your team?",
                "ideal_answer": "I motivate my team by setting clear goals, recognizing achievements, and providing opportunities for professional development."
            },
            {
                "question": "How do you prioritize tasks in a project?",
                "ideal_answer": "I prioritize tasks based on deadlines, impact, and dependencies. I use project management tools to keep track of progress and adjust priorities as needed."
            },
            {
                "question": "How do you handle feedback?",
                "ideal_answer": "I view feedback as an opportunity for growth. I listen actively, ask clarifying questions, and implement changes based on constructive criticism."
            },
            {
                "question": "What strategies do you use for effective communication?",
                "ideal_answer": "I use clear and concise language, active listening, and regular check-ins to ensure effective communication within the team."
            },
            {
                "question": "How do you manage deadlines?",
                "ideal_answer": "I manage deadlines by setting realistic timelines, breaking tasks into smaller steps, and regularly reviewing progress to ensure we stay on track."
            },
            {
                "question": "How do you ensure quality in your work?",
                "ideal_answer": "I ensure quality by following best practices, conducting thorough testing, and seeking feedback from peers to identify areas for improvement."
            },
            {
                "question": "What do you do if a project is falling behind schedule?",
                "ideal_answer": "If a project is falling behind schedule, I assess the situation, identify bottlenecks, and communicate with the team to reallocate resources or adjust timelines as necessary."
            }
        ],
        "technical": [
            {
                "question": "What programming languages are you familiar with?",
                "ideal_answer": "I am proficient in Python, Java, and SQL. I have used these languages for various academic projects, including data analysis, building REST APIs, and database management."
            },
            {
                "question": "Can you explain the concept of object-oriented programming?",
                "ideal_answer": "Object-oriented programming is a programming paradigm based on the concept of 'objects', which can contain data and code. It allows for encapsulation, inheritance, and polymorphism."
            },
            {
                "question": "What is a database?",
                "ideal_answer": "A database is an organized collection of data that can be easily accessed, managed, and updated. It is typically managed by a Database Management System (DBMS)."
            },
            {
                "question": "What is the difference between front-end and back-end development?",
                "ideal_answer": "Front-end development involves creating the visual aspects of a website that users interact with, while back-end development focuses on server-side logic and database interactions."
            },
            {
                "question": "What is version control, and why is it important?",
                "ideal_answer": "Version control is a system that records changes to files over time, allowing multiple people to collaborate on a project. It is important for tracking changes and managing code effectively."
            },
            {
                "question": "Can you explain what an API is?",
                "ideal_answer": "An API, or Application Programming Interface, is a set of rules that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use."
            },
            {
                "question": "What is your experience with data structures?",
                "ideal_answer": "I have studied various data structures, including arrays, linked lists, stacks, and queues. I have implemented them in projects to optimize data storage and retrieval."
            },
            {
                "question": "What is a framework, and can you name a few?",
                "ideal_answer": "A framework is a pre-built collection of code that provides a foundation for developing applications. Examples include Django for Python, React for JavaScript, and Spring for Java."
            },
            {
                "question": "How do you approach debugging?",
                "ideal_answer": "I approach debugging by first reproducing the error, then using print statements or debugging tools to trace the issue. I also consult documentation and online resources for solutions."
            },
            {
                "question": "What is your experience with testing?",
                "ideal_answer": "I have experience writing unit tests and integration tests using frameworks like JUnit and pytest. I understand the importance of testing in ensuring code quality."
            }
        ],
    }

    question_pool = experienced_questions if experience_level == "Experienced" else fresher_questions

    domain_questions = question_pool.get(domain.lower(), [])

    if not domain_questions:
        return {"question": "No questions available for this domain.", "ideal_answer": "N/A"}

    import random
    selected_qna = random.choice(domain_questions)
    question = selected_qna["question"]
    ideal_answer = selected_qna["ideal_answer"]

    # print("Question:", question)
    # print("Ideal Answer:", ideal_answer)
    return question, ideal_answer

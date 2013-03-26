from setuptools import find_packages, setup

setup(
    name='TicketBranch', version='0.1',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'ticket_branch = ticket_branch.ticket_branch',
        ],
    },
)

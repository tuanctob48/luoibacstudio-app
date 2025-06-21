#!/usr/bin/env python3
"""
Script to modify Wagtail settings for PostgreSQL
"""

import os
import re

def modify_settings():
    settings_file = "luoibacstudio/luoibacstudio/settings/base.py"
    
    # Read the current settings file
    with open(settings_file, 'r') as f:
        content = f.read()
    
    # Replace the DATABASES configuration
    database_pattern = r'DATABASES\s*=\s*{[^}]*}'
    new_database_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'luoibacstudio'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
"""
    
    # Replace the database configuration
    updated_content = re.sub(database_pattern, new_database_config, content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(settings_file, 'w') as f:
        f.write(updated_content)
    
    print("Successfully updated database configuration for PostgreSQL")

if __name__ == "__main__":
    modify_settings() 
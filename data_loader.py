import json

# Simulated loader - already prepared in PDF
assessments = [
  {
    "name": "Core Java (Entry Level)",
    "url": "https://www.shl.com/solutions/products/product-catalog/view/core-java-entry-level-new/",
    "description": "Test for Java programming fundamentals and basic coding skills.",
    "remote_testing": "Yes",
    "adaptive_support": "No",
    "duration": "40 mins",
    "type": "Programming"
  },
  {
    "name": "Automata - Fix (New)",
    "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-fix-new/",
    "description": "Automated code fixing assessment for identifying logical and syntax issues.",
    "remote_testing": "Yes",
    "adaptive_support": "Yes",
    "duration": "45 mins",
    "type": "Programming"
  },
  {
    "name": "Communication Skills Test",
    "url": "https://www.shl.com/solutions/products/product-catalog/view/svar-spoken-english-indian-accent-new/",
    "description": "Evaluates spoken English, fluency, and pronunciation.",
    "remote_testing": "Yes",
    "adaptive_support": "No",
    "duration": "20 mins",
    "type": "Language"
  },
  {
    "name": "Leadership and Management Assessment",
    "url": "https://www.shl.com/solutions/products/product-catalog/view/global-skills-assessment/",
    "description": "Analyzes leadership and strategic management competencies.",
    "remote_testing": "Yes",
    "adaptive_support": "Yes",
    "duration": "60 mins",
    "type": "Cognitive"
  },
  {
    "name": "SQL Server (New)",
    "url": "https://www.shl.com/solutions/products/product-catalog/view/sql-server-new/",
    "description": "Measures knowledge of SQL queries, databases, and relational models.",
    "remote_testing": "Yes",
    "adaptive_support": "No",
    "duration": "35 mins",
    "type": "Database"
  }
]

with open("assessments.json", "w") as f:
    json.dump(assessments, f, indent=2)
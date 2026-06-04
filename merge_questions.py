#!/usr/bin/env python3
"""
Extract questions from NEW_QUESTIONDUMP.md and merge with questions.json
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any

def parse_markdown_questions(md_content: str) -> List[Dict[str, Any]]:
    """
    Parse questions from markdown format:
    **Q1:** Question text
    Option 1: Option text
    Option 2: Option text
    Option 3: Option text
    Option 4: Option text
    
    Correct Answer: Option text
    
    ---
    """
    questions = []
    
    # Split by "---" to identify question blocks
    blocks = md_content.split("---")
    
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        
        if len(lines) < 6:
            continue
        
        try:
            # First line should be **Q?: Question text**
            first_line = lines[0]
            if not first_line.startswith('**Q'):
                continue
            
            # Extract question text (everything after the Q#: pattern)
            question_match = re.search(r'\*\*Q\d+:\*?\s*(.+?)(?:\*\*)?$', first_line, re.IGNORECASE)
            if not question_match:
                continue
            question_text = question_match.group(1).strip()
            
            # Extract options and correct answer
            options = []
            correct_answer_text = None
            
            for line in lines[1:]:
                if line.lower().startswith('correct answer:'):
                    correct_answer_text = line.split(':', 1)[1].strip()
                elif re.match(r'option\s+\d+:', line, re.IGNORECASE):
                    # Extract option text
                    option_text = re.sub(r'option\s+\d+:\s*', '', line, flags=re.IGNORECASE).strip()
                    options.append(option_text)
            
            # Validate we have all required fields
            if question_text and len(options) == 4 and correct_answer_text:
                # Find which option matches the correct answer
                correct_index = None
                for i, option in enumerate(options):
                    if option.lower() == correct_answer_text.lower():
                        correct_index = i
                        break
                
                if correct_index is not None:
                    question_obj = {
                        "question": question_text,
                        "options": options,
                        "correctAnswerIndex": correct_index
                    }
                    questions.append(question_obj)
        
        except Exception as e:
            continue
    
    return questions


def load_existing_questions(json_path: str) -> List[Dict[str, Any]]:
    """Load existing questions from JSON file."""
    if not Path(json_path).exists():
        return []
    
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {json_path}")
            return []


def normalize_question_text(text: str) -> str:
    """Normalize question text for comparison (lowercase, remove extra whitespace)."""
    return ' '.join(text.lower().split())


def deduplicate_questions(new_questions: List[Dict], existing_questions: List[Dict]) -> tuple:
    """
    Deduplicate by comparing question text (case-insensitive).
    Returns: (merged_questions, duplicate_count)
    """
    # Create a set of normalized existing question texts
    existing_normalized = {normalize_question_text(q['question']): q for q in existing_questions}
    
    # Track duplicates
    duplicates = 0
    merged = list(existing_questions)
    
    # Add new questions that don't already exist
    for new_q in new_questions:
        normalized_new = normalize_question_text(new_q['question'])
        
        if normalized_new not in existing_normalized:
            merged.append(new_q)
        else:
            duplicates += 1
    
    return merged, duplicates


def main():
    """Main function to orchestrate the extraction and merge."""
    workspace = Path("c:\\Users\\samue\\Documents\\isc2 CC")
    md_file = workspace / "170+ ISC2 CC Dump Questions.md"  # Using the main dump file
    json_file = workspace / "questions.json"
    
    # Read markdown file
    print(f"Reading {md_file}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Parse new questions
    print("Parsing questions from markdown...")
    new_questions = parse_markdown_questions(md_content)
    
    # Load existing questions
    print(f"Loading existing questions from {json_file}...")
    existing_questions = load_existing_questions(str(json_file))
    
    # Deduplicate
    print("Deduplicating questions...")
    merged_questions, duplicates = deduplicate_questions(new_questions, existing_questions)
    
    # Write merged questions
    print(f"Writing merged questions to {json_file}...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(merged_questions, f, indent=2, ensure_ascii=False)
    
    # Report statistics
    print("\n" + "="*60)
    print("MERGE REPORT")
    print("="*60)
    print(f"Questions extracted from markdown: {len(new_questions)}")
    print(f"Existing questions in JSON:        {len(existing_questions)}")
    print(f"Duplicates found:                  {duplicates}")
    print(f"New unique questions added:        {len(new_questions) - duplicates}")
    print(f"Final total in questions.json:     {len(merged_questions)}")
    print("="*60)


if __name__ == "__main__":
    main()

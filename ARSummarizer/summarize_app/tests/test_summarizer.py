from django.test import TestCase
from summarize_app.summarizer.summarize import get_llm_response, read_document
from summarize_app import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class SummarizeTestCase(TestCase):
    """
    Test case for the summarization functionality.
    """

    def test_read_pdf(self):
        """
        Test reading and extracting text content from a PDF file.
        """
        with open('test_files/sample.pdf', 'rb') as pdf_file:
            pdf_content = pdf_file.read()
        file_extension = "pdf"
        expected_text = "This is a sample pdf file for testing  "
        self.assertEqual(read_document(pdf_content, file_extension), expected_text)

    def test_read_docx(self):
        """
        Test reading and extracting text content from a DOCX file.
        """
        with open('test_files/sample.docx', 'rb') as docx_file:
            docx_content = docx_file.read()
        file_extension = "docx"
        expected_text = "This is a sample docx file for testing"
        self.assertEqual(read_document(docx_content, file_extension), expected_text)

    def test_get_llm_response(self):
        """
        Test generating a summary for a given input content and verifying the summary
        by asking a relevant yes/no question.
        """
        # Input content to summarize
        input_content = (
            "Sachin Tendulkar, often hailed as the 'Master Blaster,' is a legendary Indian cricketer known for his "
            "incredible batting skills and numerous records, including being the highest run-scorer in both Test and One "
            "Day International cricket. Throughout his 24-year career, he amassed over 34,000 international runs and 100 "
            "centuries, earning him widespread acclaim and admiration from fans and peers alike. Tendulkar's contributions "
            "to cricket have made him an iconic figure in the sport, celebrated for his dedication, sportsmanship, and humility."
        )

        # Summarize prompt
        summary_prompt = "Summarize this : {input_content}"
        prompt = PromptTemplate(
            template=summary_prompt,
            input_variables=["input_content"]
        )

        # Initialize LLM and chain for summarization
        summary_llm = ChatOpenAI(
                    model_name=config.openai_llm_name,
                    openai_api_key=config.API_KEY,
                    temperature=0
        )
        chain = LLMChain(llm=summary_llm, prompt=prompt)

        # Generate summary
        llm_response_summary = chain.run({
            'input_content': input_content
        })
        output_content = llm_response_summary

        # Test question to verify summary
        test_question = "Is Sachin Tendulkar known as Master Blaster?"
        test_question_prompt = (
            "given this : " + output_content + " , please answer this question only in YES or NO : {uploaded_file}"
        )
        prompt = PromptTemplate(
            template=test_question_prompt,
            input_variables=["uploaded_file"]
        )

        # Initialize LLM and chain for question answering
        test_llm = ChatOpenAI(
                    model_name=config.openai_llm_name,
                    openai_api_key=config.API_KEY,
                    temperature=0
        )
        
        test_chain = LLMChain(llm=test_llm, prompt=prompt)

        # Verify the response to the question
        self.assertEqual(get_llm_response(test_chain, test_question), 'YES')

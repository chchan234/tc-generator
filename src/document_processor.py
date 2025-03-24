"""
문서 처리 모듈 - 기획서 파일(PDF, DOCX) 업로드 처리를 담당
"""
import os
from pathlib import Path


class DocumentProcessor:
    """문서 파일 처리 클래스"""
    
    def __init__(self):
        self.supported_extensions = ['.pdf', '.docx']
        self.file_path = None
        
    def validate_file(self, file_path):
        """
        파일 유효성 검사
        
        Args:
            file_path (str): 검사할 파일 경로
            
        Returns:
            bool: 유효한 파일인지 여부
        """
        if not os.path.exists(file_path):
            return False, "파일이 존재하지 않습니다."
        
        ext = Path(file_path).suffix.lower()
        if ext not in self.supported_extensions:
            return False, f"지원되지 않는 파일 형식입니다. 지원 형식: {', '.join(self.supported_extensions)}"
        
        return True, "유효한 파일입니다."
    
    def load_document(self, file_path):
        """
        문서 파일 로드
        
        Args:
            file_path (str): 로드할 파일 경로
            
        Returns:
            bool: 로드 성공 여부
        """
        is_valid, message = self.validate_file(file_path)
        if not is_valid:
            print(f"오류: {message}")
            return False
        
        self.file_path = file_path
        print(f"파일 로드 성공: {file_path}")
        return True

    def get_file_extension(self):
        """
        현재 로드된 파일의 확장자 반환
        
        Returns:
            str: 파일 확장자
        """
        if not self.file_path:
            return None
        
        return Path(self.file_path).suffix.lower()
"""
Chunker 모듈 - 긴 텍스트를 처리 가능한 단위로 나누고 중복을 처리
"""
import re


class Chunker:
    """텍스트 청킹 및 요약 처리 클래스"""
    
    def __init__(self):
        self.chunks = []
        self.chunk_size = 4000  # 기본 청크 크기
        self.overlap = 200  # 청크 간 중복 크기
        self.summary = ""
    
    def set_chunk_parameters(self, chunk_size=None, overlap=None):
        """
        청크 매개변수 설정
        
        Args:
            chunk_size (int, optional): 청크 크기
            overlap (int, optional): 청크 간 중복 크기
        """
        if chunk_size is not None:
            self.chunk_size = chunk_size
        if overlap is not None:
            self.overlap = overlap
    
    def split_into_chunks(self, text):
        """
        텍스트를 청크로 분할
        
        Args:
            text (str): 분할할 텍스트
            
        Returns:
            list: 텍스트 청크 목록
        """
        if not text:
            return []
        
        # 청크 크기가 중복 크기보다 작은 경우 조정
        if self.chunk_size <= self.overlap:
            self.chunk_size = self.overlap * 2
        
        # 문단 경계를 존중하여 텍스트를 분할
        # 줄바꿈 또는 마침표 + 공백으로 문단 경계를 식별
        paragraphs = re.split(r'(\n+|\.\s+)', text)
        chunks = []
        current_chunk = ""
        
        for i in range(0, len(paragraphs), 2):
            paragraph = paragraphs[i]
            # 경계도 포함
            delimiter = paragraphs[i + 1] if i + 1 < len(paragraphs) else ""
            
            # 현재 청크 + 새 문단 길이가 청크 크기를 초과하면 새 청크 생성
            if len(current_chunk) + len(paragraph) + len(delimiter) > self.chunk_size:
                if current_chunk:
                    chunks.append(current_chunk)
                
                # 이전 청크의 끝 부분을 새 청크에 포함 (중복)
                if current_chunk and len(current_chunk) > self.overlap:
                    current_chunk = current_chunk[-self.overlap:] + paragraph + delimiter
                else:
                    current_chunk = paragraph + delimiter
            else:
                current_chunk += paragraph + delimiter
        
        # 마지막 청크 추가
        if current_chunk:
            chunks.append(current_chunk)
        
        self.chunks = chunks
        return chunks
    
    def split_by_sections(self, text):
        """
        섹션 제목을 기준으로 텍스트 분할
        
        Args:
            text (str): 분할할 텍스트
            
        Returns:
            list: 텍스트 청크 목록
        """
        if not text:
            return []
        
        # 숫자나 알파벳으로 시작하는 섹션 제목 패턴 (ex: "1. ", "1.1 ", "A. ", "a) ")
        section_pattern = r'\n\s*(?:\d+\.[\d\.]*|\w+[\.\):])\s+[A-Z가-힣]'
        
        # 섹션 경계 찾기
        section_boundaries = [0]
        for match in re.finditer(section_pattern, text):
            if match.start() > 0:
                section_boundaries.append(match.start())
        
        # 텍스트 끝도 경계에 추가
        section_boundaries.append(len(text))
        
        # 섹션 경계를 기준으로 텍스트 분할
        sections = []
        for i in range(len(section_boundaries) - 1):
            start = section_boundaries[i]
            end = section_boundaries[i + 1]
            section_text = text[start:end]
            
            # 섹션이 너무 길면 추가 분할
            if len(section_text) > self.chunk_size:
                split_sections = self.split_into_chunks(section_text)
                sections.extend(split_sections)
            else:
                sections.append(section_text)
        
        self.chunks = sections
        return sections
    
    def get_chunked_text(self):
        """
        청킹된 텍스트 목록 반환
        
        Returns:
            list: 청킹된 텍스트 목록
        """
        return self.chunks
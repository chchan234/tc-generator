"""
exe 파일 생성 스크립트
"""
import subprocess
import os
import shutil
import sys

def get_current_directory():
    """현재 디렉토리 반환"""
    return os.path.dirname(os.path.abspath(__file__))

def clean_build_folders():
    """빌드 폴더 정리"""
    build_dirs = ['build', 'dist']
    current_dir = get_current_directory()
    
    for dir_name in build_dirs:
        dir_path = os.path.join(current_dir, dir_name)
        if os.path.exists(dir_path):
            print(f"기존 {dir_name} 폴더 삭제 중...")
            shutil.rmtree(dir_path)
    
    # spec 파일도 정리
    spec_file = os.path.join(current_dir, "tc_generator.spec")
    if os.path.exists(spec_file):
        print("기존 spec 파일 삭제 중...")
        os.remove(spec_file)

def create_exe():
    """exe 파일 생성"""
    current_dir = get_current_directory()
    
    # 작업 디렉토리를 스크립트 위치로 변경
    os.chdir(current_dir)
    
    print("현재 작업 디렉토리:", os.getcwd())
    print("app.py 파일 존재 여부:", os.path.exists("app.py"))
    
    print("빌드 폴더 정리 중...")
    clean_build_folders()
    
    print("PyInstaller로 exe 파일 생성 중...")
    
    try:
        # app.py 파일의 전체 경로
        app_path = os.path.join(current_dir, "app.py")
        if not os.path.exists(app_path):
            print(f"오류: {app_path} 파일을 찾을 수 없습니다.")
            return 1
        
        print(f"app.py 파일 경로: {app_path}")
        
        # PyInstaller 명령어 구성
        pyinstaller_cmd = [
            'pyinstaller',
            '--noconfirm',
            '--onedir',  # onefile 대신 onedir 사용
            '--windowed',
            '--name', 'tc_generator',
            '--add-data', f'templates{os.pathsep}templates',
            '--add-data', f'static{os.pathsep}static',
            '--add-binary', f'output{os.pathsep}output',
            # 필요한 패키지 명시적으로 포함
            '--hidden-import=pandas',
            '--hidden-import=openpyxl',
            '--hidden-import=PyPDF2',
            '--hidden-import=docx',
            '--hidden-import=PyQt5',
            '--hidden-import=langchain',
            '--hidden-import=langchain_google_genai',
            '--hidden-import=google.generativeai',
            '--hidden-import=langgraph',
            # 콘솔 창 표시 (디버그용)
            '--console',
            app_path
        ]
        
        # icon 파일이 있으면 추가
        icon_path = os.path.join(current_dir, 'static', 'icon.ico')
        if os.path.exists(icon_path):
            pyinstaller_cmd.extend(['--icon', icon_path])
        
        # PyInstaller 실행
        subprocess.run(pyinstaller_cmd, check=True)
        
        print("\n빌드 성공!")
        print(f"\n실행 파일 위치: {os.path.join(current_dir, 'dist', 'tc_generator', 'tc_generator.exe')}")
        
        # 출력 디렉토리 생성 확인
        dist_output_dir = os.path.join(current_dir, 'dist', 'tc_generator', 'output')
        if not os.path.exists(dist_output_dir):
            os.makedirs(dist_output_dir)
            print("output 디렉토리 생성됨")
        
        return 0
    except subprocess.CalledProcessError as e:
        print(f"\n빌드 실패! 오류: {str(e)}")
        return 1
    except Exception as e:
        print(f"\n빌드 실패! 오류: {str(e)}")
        return 1

if __name__ == "__main__":
    print("테스트 케이스 생성기 EXE 파일 빌드 시작...\n")
    sys.exit(create_exe())
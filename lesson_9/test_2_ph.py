from pydoc import text
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("http://5.101.50.27:8000/docs")
db = CompanyTable("postgresql://harrypotter:$2b$12$2u7ym.MScKQiJFiJhxB06.1yJIiJ0FfMwe75ZhbCaDqIG9pAJzOs2@5.101.50.27:5432/x_clients")


def test_get_companies():
    #Шаг1: получить список компаний через API:
    api_result = api.get_company_list()

    #Шаг2: получить список компаний из БД:
    db_result = db.get_companies()

    #Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)

def get_active_companies(self):
        conn = self.db.connect()
        result = conn.execute(
            text("SELECT * FROM company "
                 "WHERE \"is_active\" = true  "
                 "AND deleted_at IS NULL")
        )
        rows = result.mappings().all()
        conn.close()
        return rows

def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()

    assert len(filtered_list) == len(db_list)
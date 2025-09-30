from category import Category

def test_serialization():
    """Testa a funcionalidade de serialização"""
    print("=== TESTE DE SERIALIZAÇÃO ===")
    
    # Cria uma categoria original
    original_category = Category(
        id="cat-001",
        name="Electronics",
        description="Electronic devices and accessories"
    )
    
    print(f"Categoria original: {original_category.name}")
    print(f"ID: {original_category.id}")
    print(f"Ativa: {original_category.is_active}")
    
    # Exporta para dicionário
    category_dict = original_category.to_dict()
    print(f"\nDicionário exportado: {category_dict}")
    
    # Reconstrói a partir do dicionário
    reconstructed_category = Category.from_dict(category_dict)
    
    # Verifica equivalência
    print(f"\nVerificação de equivalência:")
    print(f"IDs iguais: {original_category.id == reconstructed_category.id}")
    print(f"Nomes iguais: {original_category.name == reconstructed_category.name}")
    print(f"Descrições iguais: {original_category.description == reconstructed_category.description}")
    print(f"Estados ativos iguais: {original_category.is_active == reconstructed_category.is_active}")
    
    return original_category, reconstructed_category

def test_domain_events():
    """Testa o sistema de eventos de domínio"""
    print("\n=== TESTE DE EVENTOS DE DOMÍNIO ===")
    
    # Cria uma nova categoria
    category = Category(
        id="cat-002",
        name="Books",
        description="All kinds of books"
    )
    
    print(f"Eventos após criação: {len(category.events)}")
    for event in category.events:
        print(f"  - {event.event_type} em {event.timestamp}")
    
    # Atualiza a categoria
    category.update(name="Books & Literature", description="Books and literary works")
    print(f"\nEventos após atualização: {len(category.events)}")
    for event in category.events[-1:]:
        print(f"  - {event.event_type} em {event.timestamp}")
        if hasattr(event, 'updated_fields'):
            print(f"    Campos atualizados: {event.updated_fields}")
    
    # Desativa a categoria
    category.deactivate()
    print(f"\nEventos após desativação: {len(category.events)}")
    for event in category.events[-1:]:
        print(f"  - {event.event_type} em {event.timestamp}")
    
    # Ativa a categoria
    category.activate()
    print(f"\nEventos após ativação: {len(category.events)}")
    for event in category.events[-1:]:
        print(f"  - {event.event_type} em {event.timestamp}")
    
    # Demonstra processamento de eventos
    print(f"\n=== PROCESSAMENTO DE EVENTOS ===")
    events = category.get_events()
    print(f"Total de eventos para processar: {len(events)}")
    
    for i, event in enumerate(events, 1):
        print(f"{i}. {event.event_type} - Categoria: {event.category_id}")
    
    # Limpa eventos após processamento
    category.clear_events()
    print(f"\nEventos após limpeza: {len(category.events)}")

def test_error_scenarios():
    """Testa cenários de erro"""
    print("\n=== TESTE DE CENÁRIOS DE ERRO ===")
    
    try:
        # Testa reconstrução com dados inválidos
        invalid_data = {
            'class_name': 'InvalidClass',
            'id': 'test',
            'name': 'Test',
            'description': 'Test',
            'is_active': True
        }
        Category.from_dict(invalid_data)
    except ValueError as e:
        print(f"Erro esperado na reconstrução: {e}")
    
    try:
        # Testa reconstrução com campos faltantes
        incomplete_data = {
            'class_name': 'Category',
            'id': 'test',
            'name': 'Test'
            # description e is_active faltando
        }
        Category.from_dict(incomplete_data)
    except ValueError as e:
        print(f"Erro esperado em campos faltantes: {e}")
    
    try:
        # Testa validação de nome vazio
        Category(id="cat-003", name="", description="Test")
    except ValueError as e:
        print(f"Erro esperado na validação: {e}")
    
    try:
        # Testa validação de nome muito longo
        Category(id="cat-004", name="A" * 256, description="Test")
    except ValueError as e:
        print(f"Erro esperado no tamanho do nome: {e}")

if __name__ == "__main__":
    # Executa todos os testes
    test_serialization()
    test_domain_events()
    test_error_scenarios()
    
    print("\n=== DEMONSTRAÇÃO CONCLUÍDA ===")
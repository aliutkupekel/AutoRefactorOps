from mcp_bus.acl_verifier import MCPGovernanceBus
from agents.discovery_agent import CodeDiscoveryAgent
from agents.generator_agent import RefactoringGeneratorAgent

def main():
    print("=== AutoRefactorOps System Starting ===")
    
    # 1. Initialize MCP Bus
    mcp_bus = MCPGovernanceBus()
    
    # 2. Initialize Agents
    discovery = CodeDiscoveryAgent()
    generator = RefactoringGeneratorAgent()
    
    # 3. Simulate Workflow
    target_file = "target_repo/sample_code.py"
    if mcp_bus.verify_request(discovery, "READ"):
        debt_data = discovery.scan_target(target_file)
        
        if mcp_bus.verify_request(generator, "DRAFT"):
            draft = generator.draft_optimization(debt_data)
            print("=== Cycle Complete ===")

if __name__ == "__main__":
    main()
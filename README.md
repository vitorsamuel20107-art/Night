local Players = game:GetService("Players")
local player = Players.LocalPlayer

-- 1. Cria a Interface Principal
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "AvisoManutencao"
screenGui.ResetOnSpawn = false
screenGui.Parent = player:WaitForChild("PlayerGui")

-- 2. Janela de Aviso (Centro da tela)
local janela = Instance.new("Frame")
janela.Size = UDim2.new(0, 350, 0, 150)
janela.Position = UDim2.new(0.5, -175, 0.5, -75)
janela.BackgroundColor3 = Color3.fromRGB(30, 30, 30) -- Cinza escuro
janela.BorderSizePixel = 0
janela.Parent = screenGui

-- Arredondar cantos da janela
local corner = Instance.new("UICorner")
corner.CornerRadius = UDim.new(0, 8)
corner.Parent = janela

-- 3. Texto do Aviso
local texto = Instance.new("TextLabel")
texto.Size = UDim2.new(1, 0, 1, 0)
texto.BackgroundTransparency = 1
texto.Text = "Script em manutenção"
texto.TextColor3 = Color3.fromRGB(255, 255, 255)
texto.Font = Enum.Font.GothamMedium
texto.TextSize = 22
texto.Parent = janela

-- 4. Botão de Fechar (X)
local botaoFechar = Instance.new("TextButton")
botaoFechar.Size = UDim2.new(0, 30, 0, 30)
botaoFechar.Position = UDim2.new(1, -35, 0, 5)
botaoFechar.BackgroundColor3 = Color3.fromRGB(200, 50, 50) -- Vermelho
botaoFechar.Text = "X"
botaoFechar.TextColor3 = Color3.fromRGB(255, 255, 255)
botaoFechar.Font = Enum.Font.GothamBold
botaoFechar.TextSize = 16
botaoFechar.Parent = janela

-- Arredondar cantos do botão X
local botaoCorner = Instance.new("UICorner")
botaoCorner.CornerRadius = UDim.new(0, 6)
botaoCorner.Parent = botaoFechar

-- 5. Função para fechar ao clicar no X
botaoFechar.MouseButton1Click:Connect(function()
    screenGui:Destroy()
end)
